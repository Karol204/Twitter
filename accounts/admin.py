from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from base_app.models import Tweet
# Register your models here.


CustomUser = get_user_model()

class TweetAdmin(admin.ModelAdmin):
    pass


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = get_user_model()
    list_display = ['email', 'username']


admin.site.register(Tweet, TweetAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
