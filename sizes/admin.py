from django.contrib import admin
from .models import SizeType

@admin.register(SizeType)
class SizeTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')  # Show name and ID in the list view
    list_display_links = ('name',)  # Make the name clickable for editing
    search_fields = ('name',)  # Enable search by size name
    ordering = ('name',)  # Order sizes alphabetically
    list_per_page = 20  # Paginate with 20 sizes per page
