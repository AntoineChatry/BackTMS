from django.contrib import admin
from .models import TMS

class TmsAdmin(admin.ModelAdmin):
    list_display = ('classroom', 'building', 'completed', 'seats', 'rows', 'columns')
    
# Register your models here.
admin.site.site_header = "TrackMySeat Administration"

admin.site.register(TMS, TmsAdmin)