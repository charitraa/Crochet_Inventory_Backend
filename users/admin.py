from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User

class CustomUserAdmin(UserAdmin):
    """
    Custom Admin Panel for User Management
    """
    list_display = ('id', 'full_name', 'email', 'username', 'phone_number', 'is_staff', 'is_active')  
    list_filter = ('is_staff', 'is_active', 'is_superuser')  
    search_fields = ('email', 'username', 'full_name', 'phone_number')  
    ordering = ('full_name',)  
    readonly_fields = ('last_login', 'date_joined')  # Prevent modification

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('full_name', 'username', 'phone_number', 'address', 'profile_pic')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name', 'username', 'phone_number', 'address', 'email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )

    def profile_pic_preview(self, obj):
        """ Show a preview of profile pic in admin panel """
        if obj.profile_pic:
            return f'<img src="{obj.profile_pic.url}" width="50" height="50" style="border-radius: 50%;" />'
        return "No Image"
    profile_pic_preview.allow_tags = True  # Enable HTML rendering
    profile_pic_preview.short_description = "Profile Picture"


admin.site.register(User, CustomUserAdmin)
