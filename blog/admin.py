from django.contrib import admin
from .models import POST

# Register your models here.

class POSTAdmin(admin.ModelAdmin):
    model = POST
    list_display = [
        'author',
        'title',
        'published_date'
    ]

admin.site.register(POST, POSTAdmin)