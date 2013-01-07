from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.admin import ModelAdmin

from tracking.apps.users.models import UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    max_num = 1
    can_delete = False
    verbose_name_plural = 'Profile information'

class UserAdmin(UserAdmin):
	inlines = (UserProfileInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)