from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    #list display
    list_display = ('title', 'id', 'slug', 'date_pub')
    #search list
    search_fields = ['title']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'slug')
