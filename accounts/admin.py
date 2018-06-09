from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Vedios

# Register your models here.
class VediosAdmin(admin.ModelAdmin):
	class Meta():
		model=Vedios
	list_display=["name","updated","vedio"]
admin.site.register(Vedios,VediosAdmin)
