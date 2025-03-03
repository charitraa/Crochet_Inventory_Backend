from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')  # Display fields in the list view
    list_display_links = ('name',)  # Make name clickable
    search_fields = ('name',)  # Enable search functionality
    ordering = ('name',)  # Order by name in ascending order
    list_per_page = 20  # Limit items per page for better performance
