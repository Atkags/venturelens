from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import RegisterSerializer, UserSerializer, ChangePasswordSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class RegisterView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = RegisterSerializer

class MeView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request):
    serializer = UserSerializer(request.user)

    return Response(
      serializer.data
    )

  def patch(self, request):
    serializer = UserSerializer(
      request.user,
      data=request.data,
      partial=True
    )

    serializer.is_valid(
      raise_exception=True
    )

    serializer.save()

    return Response(
      serializer.data
    )

class ChangePasswordView(APIView):
  permission_classes = [IsAuthenticated]

  def post(self, request):
    serializer = ChangePasswordSerializer(
      data=request.data,
      context={"request": request}
    )

    serializer.is_valid(
      raise_exception=True
    )

    serializer.save()

    return Response({
      "message": "Password changed successfully"
    })