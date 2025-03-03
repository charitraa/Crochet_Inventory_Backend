from django.contrib import admin
from .models import ColorType

@admin.register(ColorType)
class ColorTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')  # Show name and ID in the list view
    list_display_links = ('name',)  # Make the name clickable for editing
    search_fields = ('name',)  # Enable search by color name
    ordering = ('name',)  # Order colors alphabetically
    list_per_page = 20  # Paginate with 20 colors per page
