from django.contrib import admin
from .models import Contact, Teachers, Notice, Events

# Register your models here.
admin.site.register(Contact)
admin.site.register(Teachers)
admin.site.register(Notice)
admin.site.register(Events)
