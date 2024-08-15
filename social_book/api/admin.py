from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    # Define the fields to be displayed in the admin interface
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('full_name', 'gender', 'city', 'state')}),
        ('Credit Card Information', {'fields': ('credit_card_type', 'credit_card_number', 'cvc', 'expiration_date')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Fields to be used in creating and editing the user model
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'full_name', 'gender', 'city', 'state', 'credit_card_type', 'credit_card_number', 'cvc', 'expiration_date'),
        }),
    )

    # Fields to display in the list view
    list_display = ('username', 'email', 'full_name', 'gender', 'city', 'state', 'is_staff')
    search_fields = ('username', 'email', 'full_name', 'city', 'state')
    ordering = ('username',)

# Register the custom user admin class with the User model
admin.site.register(User, CustomUserAdmin)
