from django.contrib import admin
from .models import Book
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'author_name')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'price')
    fields = ('name', 'price', 'author_name')
    save_on_top = True
    list_filter = ('price', 'name')



