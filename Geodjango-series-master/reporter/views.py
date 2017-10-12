from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Counties,Incidences,Wells,Farms
# Create your views here.
class HomePageView(TemplateView):
	template_name = 'index.html'

def wells_datasets(request):
	wells = serialize('geojson', Wells.objects.all())
	return HttpResponse(wells, content_type='json')

def farms_datasets(request):
        farms = serialize('geojson', Farms.objects.all())
        return HttpResponse(farms, content_type='json')

def county_datasets(request):
	counties = serialize('geojson', Counties.objects.all())
	return HttpResponse(counties,content_type='json')

def point_datasets(request):
	points = serialize('geojson', Incidences.objects.all())
	return HttpResponse(points,content_type='json')
