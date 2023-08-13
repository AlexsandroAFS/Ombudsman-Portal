from django.contrib import admin
from .models import *


# Register your models here.
class OmbudsmanStatusAdmin(admin.ModelAdmin):
    list_display = ('ost_title', 'ost_description', 'ost_create_date')


admin.site.register(OmbudsmanStatus, OmbudsmanStatusAdmin)
