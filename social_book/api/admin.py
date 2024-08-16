from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'full_name', 'gender', 'credit_card_type', 
        'credit_card_number', 'cvc', 'expiration_date', 'public_visibility', 
        'age', 'birth_year', 'address', 'is_staff'
    )
    search_fields = ('username', 'email', 'full_name', 'credit_card_number', 'address')
    ordering = ('username',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('full_name', 'email', 'gender', 'age', 'birth_year', 'address')}),
        ('Credit Card Info', {'fields': ('credit_card_type', 'credit_card_number', 'cvc', 'expiration_date')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Visibility', {'fields': ('public_visibility',)}),
    )

admin.site.register(User, CustomUserAdmin)
