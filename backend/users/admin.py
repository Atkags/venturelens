from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class UserProfileInLine(admin.StackedInline):
  model = UserProfile
  can_delete = False
  extra = 0

class CustomUserAdmin(UserAdmin):
  inlines = [UserProfileInLine]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)