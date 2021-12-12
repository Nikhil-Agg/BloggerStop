from django.contrib import admin
from .models import Category, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_no', 'last_modified', 'category')
    list_per_page = 10
    list_editable = ('category',)
    list_display_links = ('title',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)