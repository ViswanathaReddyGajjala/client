from django.contrib import admin
from .models import Incidences, Counties
from .models import Houses,Members,Farms,Wells,Crops,Yields
#from django.contrib.gis.db import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

class IncidencesAdmin(LeafletGeoAdmin):
	#pass
	list_display =('name','location')

class CountiesAdmin(LeafletGeoAdmin):
	#pass
	list_display =('counties','codes')

class HousesAdmin(LeafletGeoAdmin):
	list_display = ('point', 'income')

class MembersAdmin(LeafletGeoAdmin):
	list_display = ('Name', 'Age')

class FarmsAdmin(LeafletGeoAdmin):
	list_display = ('HID','area')

class CropsAdmin(LeafletGeoAdmin):
	list_display = ('Name', 'Seasons')

class WellsAdmin(LeafletGeoAdmin):
	list_display = ('HID', 'point')

class YieldsAdmin(LeafletGeoAdmin):
	list_display = ('WID', 'Yield')

admin.site.register(Incidences, IncidencesAdmin)
admin.site.register(Counties, CountiesAdmin)
admin.site.register(Houses, HousesAdmin)
admin.site.register(Members, MembersAdmin)
admin.site.register(Farms,FarmsAdmin)
admin.site.register(Crops,CropsAdmin)
admin.site.register(Wells,WellsAdmin)
admin.site.register(Yields,YieldsAdmin)
