from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import RegistrationSerializer, UserSerializer


class RegistrationAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"user": UserSerializer(user).data, "token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        username = request.data.get("username", "").strip()
        password = request.data.get("password", "").strip()
        if not username or not password:
            return Response({"error": "يرجى إدخال اسم المستخدم وكلمة المرور"}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(request, username=username, password=password)
        if user is None:
            return Response({"error": "اسم المستخدم أو كلمة المرور غير صحيحة"}, status=status.HTTP_401_UNAUTHORIZED)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"user": UserSerializer(user).data, "token": token.key})
