from django.contrib import admin
from accounts.models import User,Profile
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("email", "is_staff", "is_active",'is_author','is_superuser','is_Instructors')
    list_filter = ("email", "is_staff", "is_active",'is_author','is_superuser','is_Instructors')
    ordering = ('-email',)
    fieldsets = (
        ('Authentication', {'fields': ('email', 'password')}),
        ('Permission', {'fields': ('is_staff', 'is_author', 'is_active', 'is_superuser','is_Instructors')}),
        ('Group_permission', {'fields': ('groups', 'user_permissions')}),
        ('Important_Date', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_author", "is_active"
            )}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)