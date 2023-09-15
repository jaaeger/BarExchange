from django.contrib import admin

from .models import Comments


# Register your models here.
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'rate', 'created_at', 'updated_at', 'is_published', 'bar')
    list_display_links = ('id',)
    search_fields = ('rate', 'created_at', 'updated_at')

admin.site.register(Comments, CommentsAdmin)
