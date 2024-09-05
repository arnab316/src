from django.contrib import admin
from .models import Post
# Register your models here.

'''
In Django, the @admin.register(Post) decorator is a more concise and preferred way to register your models with the Django admin interface.
It essentially connects your model with Django’s admin panel, 
allowing you to manage that model through the Django admin site.
'''
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    show_facets = admin.ShowFacets.ALWAYS