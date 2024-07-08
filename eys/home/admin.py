from django.contrib import admin
from django.db import models
from home.models import Setting
from home.models import ContactFormMessage
class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'status']
    list_filter = ['status']



admin.site.register(ContactFormMessage,ContactFormMessageAdmin)
admin.site.register(Setting)
