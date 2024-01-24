from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'service_icon']

    def service_icon(self, obj):
        return format_html(f"<i class='{obj.icon}'></i>")

admin.site.register(Service, ServiceAdmin)