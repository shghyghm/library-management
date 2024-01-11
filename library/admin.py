from django.contrib import admin
from .models import Author, Book




@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    list_display = ('name', 'birth_date', 'bio', 'created_at', 'updated_at', 'user')
    list_filter = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = ('title', 'genre', 'publication_date', 'availability_status', 'created_at', 'updated_at', 'user')
    list_filter = ('title', 'genre', 'publication_date', 'availability_status', 'authors')
    search_fields = ('title', 'genre', 'authors')