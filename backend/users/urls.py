from django.urls import path
from .views import RegisterView, MeView, ChangePasswordView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
  path("register/", RegisterView.as_view(), name="register"),
  path("me/", MeView.as_view(), name="me"),
  path("login/", TokenObtainPairView.as_view(), name="login"),
  path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
  path("change-password/", ChangePasswordView.as_view(), name="change_password"),
]