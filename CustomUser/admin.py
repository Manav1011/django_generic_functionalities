from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import CustomUser,BackupCodes
from .forms import CustomUserCreationForm,CustomUserChangeForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ('email','secret','is_staff','is_active')
    list_filter = ('email','secret','is_staff','is_active')

    fieldsets = (
        (None, {
            "fields": (
                'email','password','secret','email_verified',
            ),
        }),('Permissions',{
            'fields':('is_staff','is_active')
        })
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

    search_fields = ('email',)
    readonly_fields = ('secret',)
    ordering = ('email',)    
    
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(BackupCodes)
