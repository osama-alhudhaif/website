from rest_framework import generics, permissions, serializers, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
# الإصدار 8: استيراد فئات تحديد المعدل لحماية endpoints المصادقة من الهجمات
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from django.conf import settings

from accounts.models import User, Subscription, Follow
from .serializers import (
    UserSerializer, RegistrationSerializer, LoginSerializer,
    SubscriptionSerializer, FollowSerializer
)


# الإصدار 8: معدل مخصص صارم لـ endpoints المصادقة (5 طلبات في الدقيقة للمجهولين)
class AuthRateThrottle(AnonRateThrottle):
    rate = '5/minute'
    scope = 'auth'


class RegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]
    # الإصدار 8: تطبيق تحديد المعدل على endpoint التسجيل
    throttle_classes = [AuthRateThrottle]

    def perform_create(self, serializer):
        user = serializer.save()
        # إرسال إيميل التحقق
        try:
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            frontend_url = getattr(settings, 'FRONTEND_URL', 'http://localhost:5173')
            verify_url = f"{frontend_url}/verify-email/{uid}/{token}/"
            send_mail(
                subject='تأكيد البريد الإلكتروني - أودا',
                message=f'مرحباً {user.username}،\n\nاضغط على الرابط التالي لتأكيد بريدك الإلكتروني:\n{verify_url}\n\nشكراً لانضمامك إلى منصة أودا!',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=True,
            )
        except Exception:
            pass


class VerifyEmailAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, uid, token):
        try:
            user_id = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=user_id)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response({'error': 'رابط التحقق غير صالح'}, status=status.HTTP_400_BAD_REQUEST)

        if not default_token_generator.check_token(user, token):
            return Response({'error': 'رابط التحقق منتهي الصلاحية أو غير صالح'}, status=status.HTTP_400_BAD_REQUEST)

        user.is_active = True
        user.save()
        return Response({'message': 'تم التحقق من البريد الإلكتروني بنجاح! يمكنك الآن تسجيل الدخول.'})


class PasswordResetRequestAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # الإصدار 8: تطبيق تحديد المعدل على endpoint طلب إعادة تعيين كلمة المرور
    throttle_classes = [AuthRateThrottle]

    def post(self, request):
        email = request.data.get('email', '').strip()
        if not email:
            return Response({'error': 'البريد الإلكتروني مطلوب'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            frontend_url = getattr(settings, 'FRONTEND_URL', 'http://localhost:5173')
            reset_url = f"{frontend_url}/reset-password/{uid}/{token}/"
            send_mail(
                subject='استعادة كلمة المرور - أودا',
                message=f'مرحباً {user.username}،\n\nاضغط على الرابط التالي لإعادة تعيين كلمة المرور:\n{reset_url}\n\nإذا لم تطلب هذا، تجاهل هذا الإيميل.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=True,
            )
        except User.DoesNotExist:
            pass  # لا نكشف إذا كان الإيميل موجوداً أم لا
        except Exception:
            pass  # نتجاهل أخطاء الإيميل - نرجع نفس الرسالة دائماً

        return Response({'message': 'إذا كان البريد الإلكتروني مسجلاً، ستصل رسالة الاستعادة قريباً.'})


class PasswordResetConfirmAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # الإصدار 8: تطبيق تحديد المعدل على endpoint تأكيد إعادة تعيين كلمة المرور
    throttle_classes = [AuthRateThrottle]

    def post(self, request, uid, token):
        new_password = request.data.get('new_password', '')
        if len(new_password) < 8:
            return Response({'error': 'كلمة المرور يجب أن تكون 8 أحرف على الأقل'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user_id = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=user_id)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response({'error': 'رابط إعادة التعيين غير صالح'}, status=status.HTTP_400_BAD_REQUEST)

        if not default_token_generator.check_token(user, token):
            return Response({'error': 'رابط إعادة التعيين منتهي الصلاحية'}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()
        return Response({'message': 'تم تغيير كلمة المرور بنجاح! يمكنك الآن تسجيل الدخول.'})


class ChangePasswordAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        current_password = request.data.get('current_password', '')
        new_password = request.data.get('new_password', '')

        if not request.user.check_password(current_password):
            return Response({'error': 'كلمة المرور الحالية غير صحيحة'}, status=status.HTTP_400_BAD_REQUEST)

        if len(new_password) < 8:
            return Response({'error': 'كلمة المرور الجديدة يجب أن تكون 8 أحرف على الأقل'}, status=status.HTTP_400_BAD_REQUEST)

        request.user.set_password(new_password)
        request.user.save()
        # تحديث الـ token بعد تغيير كلمة المرور
        Token.objects.filter(user=request.user).delete()
        new_token, _ = Token.objects.get_or_create(user=request.user)
        return Response({'message': 'تم تغيير كلمة المرور بنجاح', 'token': new_token.key})


class LoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    # الإصدار 8: تطبيق تحديد المعدل على endpoint تسجيل الدخول لمنع هجمات brute-force
    throttle_classes = [AuthRateThrottle]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        user_data = UserSerializer(user).data
        return Response({'token': token.key, 'user': user_data})


class ProfileAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class SubscriptionListCreateAPIView(generics.ListCreateAPIView):
    """عرض الاشتراكات وإنشاء اشتراك جديد"""
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # تحديد نوع الاشتراك المناسب
        user = self.request.user
        plan_type = self.request.data.get('plan_type', Subscription.PlanType.MONTHLY)

        # إذا كان المستخدم تعليمي، نستخدم سعر الاشتراك التعليمي
        if user.is_educational_user():
            plan_type = Subscription.PlanType.EDUCATIONAL

        serializer.save(user=user, plan_type=plan_type)


class SubscriptionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """عرض تفاصيل الاشتراك"""
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)


class CurrentSubscriptionAPIView(APIView):
    """الحصول على الاشتراك النشط الحالي"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        subscription = request.user.get_active_subscription()
        if subscription:
            serializer = SubscriptionSerializer(subscription)
            return Response(serializer.data)
        return Response({'message': 'لا يوجد اشتراك نشط'}, status=status.HTTP_404_NOT_FOUND)


class SubscriptionPricingAPIView(APIView):
    """عرض أسعار الاشتراكات"""
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        pricing = {
            'monthly': {
                'price': 1.00,
                'currency': 'USD',
                'description': 'اشتراك شهري',
            },
            'yearly': {
                'price': 10.00,
                'currency': 'USD',
                'description': 'اشتراك سنوي (وفر 17%)',
            },
            'educational': {
                'price': 5.00,
                'currency': 'USD',
                'description': 'اشتراك مركز تعليمي',
            },
        }
        return Response(pricing)


class ToggleDarkModeAPIView(APIView):
    """تبديل الوضع الداكن - متاح للجميع"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        user.dark_mode_enabled = not user.dark_mode_enabled
        user.save()
        return Response({
            'dark_mode_enabled': user.dark_mode_enabled,
            'message': 'تم تغيير الوضع بنجاح'
        })


class FollowListCreateAPIView(generics.ListCreateAPIView):
    """عرض قائمة المتابعين ومتابعة مستخدم جديد"""
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # التحقق من الاشتراك لميزة المتابعة
        if not self.request.user.has_active_subscription():
            return Follow.objects.none()
        return Follow.objects.filter(follower=self.request.user)

    def perform_create(self, serializer):
        # التحقق من الاشتراك
        if not self.request.user.has_active_subscription():
            raise permissions.PermissionDenied('يجب الاشتراك لاستخدام ميزة المتابعة')

        following_id = self.request.data.get('following')
        if not following_id:
            raise serializers.ValidationError('يجب تحديد المستخدم للمتابعة')

        try:
            following_user = User.objects.get(id=following_id)
        except User.DoesNotExist:
            raise serializers.ValidationError('المستخدم غير موجود')

        # لا يمكن متابعة نفسك
        if following_user == self.request.user:
            raise serializers.ValidationError('لا يمكنك متابعة نفسك')

        serializer.save(follower=self.request.user, following=following_user)


class UnfollowAPIView(APIView):
    """إلغاء متابعة مستخدم"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        # التحقق من الاشتراك
        if not request.user.has_active_subscription():
            return Response(
                {'error': 'يجب الاشتراك لاستخدام ميزة المتابعة'},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            follow = Follow.objects.get(
                follower=request.user,
                following_id=user_id
            )
            follow.delete()
            return Response({'message': 'تم إلغاء المتابعة بنجاح'})
        except Follow.DoesNotExist:
            return Response(
                {'error': 'لم يتم العثور على متابعة'},
                status=status.HTTP_404_NOT_FOUND
            )


class FollowersListAPIView(generics.ListAPIView):
    """عرض المتابعين للمستخدم"""
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return Follow.objects.filter(following_id=user_id)


class FollowingListAPIView(generics.ListAPIView):
    """عرض المستخدمين الذين يتابعهم المستخدم"""
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return Follow.objects.filter(follower_id=user_id)


class PublicAuthorProfileAPIView(APIView):
    """عرض ملف الكاتب للمشتركين"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_id):
        # التحقق من الاشتراك لرؤية ملف الكاتب
        if not request.user.has_active_subscription():
            return Response(
                {'error': 'يجب الاشتراك لرؤية ملف الكاتب وقصصه'},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            author = User.objects.get(id=user_id)
            # التحقق من أن المستخدم كاتب
            if author.role not in [User.Role.WRITER, User.Role.FOUNDER, User.Role.MUAASIS]:
                return Response(
                    {'error': 'هذا المستخدم ليس كاتباً'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            from stories.models import Story
            stories = Story.objects.filter(author=author, status='published')

            data = {
                'id': author.id,
                'username': author.username,
                'first_name': author.first_name,
                'last_name': author.last_name,
                'country': author.country,
                'stories_count': stories.count(),
                'followers_count': author.followers.count(),
                'stories': [
                    {
                        'id': s.id,
                        'title': s.title,
                        'genre': s.genre,
                        'created_at': s.created_at,
                    } for s in stories[:10]
                ]
            }
            return Response(data)
        except User.DoesNotExist:
            return Response(
                {'error': 'الكاتب غير موجود'},
                status=status.HTTP_404_NOT_FOUND
            )

