from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes

from accounts.models import User, Subscription, Follow
from .serializers import (
    UserSerializer, RegistrationSerializer, LoginSerializer,
    SubscriptionSerializer, FollowSerializer
)


class RegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]


class LoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]

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

