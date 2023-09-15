from django.contrib import admin

from .models import Bars


# Register your models here.
class BarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'photo', 'sum_rate', 'address', 'work_time', 'average_check',
                    'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'sum_rate', 'address', 'work_time', 'average_check')

admin.site.register(Bars, BarsAdmin)
