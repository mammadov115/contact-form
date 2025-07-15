from django.contrib import admin
from .models import ContactMessage
from django.utils import timezone
# Register your models here.

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'formatted_sended_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('sended_at',)

    def formatted_sended_at(self, obj):
        return obj.sended_at.strftime('%d-%m-%Y %H:%M')
    formatted_sended_at.short_description = 'Sended At'
# This will allow the ContactMessage model to be managed through the Django admin interface.