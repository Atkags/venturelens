from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.password_validation import validate_password

class UserProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserProfile
    fields = [
      "country",
      "company",
    ]

class UserSerializer(serializers.ModelSerializer):
  profile = UserProfileSerializer()

  class Meta:
    model = User
    fields = [
      "id",
      "username",
      "email",
      "profile",
    ]

  def update(self, instance, validated_data):
    profile_data = validated_data.pop("profile", {})
    instance.email = validated_data.get("email", instance.email)
    instance.save()
    profile = instance.profile
    profile.country = profile_data.get("country", profile.country)
    profile.company = profile_data.get("company", profile.company)
    profile.save()
    return instance

class RegisterSerializer(serializers.ModelSerializer):
  password = serializers.CharField(
    write_only=True,
    min_length=8
    )

  class Meta:
    model = User
    fields = [
      "username",
      "email",
      "password",
    ]

  def create(self, validated_data):
    user = User.objects.create_user(
      username=validated_data["username"],
      email=validated_data["email"],
      password=validated_data["password"],
    )

    UserProfile.objects.create(
      user=user
    )

    return user

class ChangePasswordSerializer(serializers.Serializer):
  old_password = serializers.CharField(required=True)
  new_password = serializers.CharField(required=True, min_length=8)

  def validate_old_password(self, value):
    user = self.context["request"].user
    if not user.check_password(value):
      raise serializers.ValidationError("Old password is not correct")
    return value

  def validate_new_password(self, value):
    user = self.context["request"].user

    validate_password(value, user)
    return value

  def save(self):
    user = self.context["request"].user
    user.set_password(self.validated_data["new_password"])

    user.save()
    return user