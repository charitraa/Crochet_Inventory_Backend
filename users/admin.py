from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'email', 'username', 'full_name', 'is_staff', 'is_active')  # Fields to display
    list_filter = ('is_staff', 'is_active', 'is_superuser')  # Filters on right side
    search_fields = ('email', 'username', 'full_name')  # Search bar
    ordering = ('email',)  # Order by email
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('full_name', 'username', 'phone_number', 'address')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )

admin.site.register(User, CustomUserAdmin)



