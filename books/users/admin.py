from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = CustUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email','username']

admin.site.register(CustomUser,CustomUserAdmin)
