from django.contrib import admin
from .models import TMS

class TmsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'places')

# Register your models here.

admin.site.register(TMS, TmsAdmin)