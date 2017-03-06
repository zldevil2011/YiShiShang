from django.contrib import admin
from app.models import Data


class DataAdmin(admin.ModelAdmin):
    list_display = ('pk', 'height', 'weight', 'bust', 'waist_circumference', 'hip_circumference', 'collect_time')

admin.site.register(Data, DataAdmin)

# Register your models here.
