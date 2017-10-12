from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Counties,Incidences,Wells,Farms
import urllib.request

# Create your views here.

class BubbleView(TemplateView):
	template_name = 'bubble.html'

class PieChartView(TemplateView):
        template_name='piechart.html'

class HomePageView(TemplateView):
	template_name = 'index.html'

def wells_datasets(request):
	wells = serialize('geojson', Wells.objects.all())
	return HttpResponse(wells, content_type='json')

def farms_datasets(request):
        farms = serialize('geojson', Farms.objects.all())
        return HttpResponse(farms, content_type='json')

def county_datasets(request):
        url = "http://10.0.3.23:1235/county_data/"
        response = urllib.request.urlopen(url)
        counties = response.read()
        #counties = serialize('geojson', Counties.objects.all())
        return HttpResponse(counties,content_type='json')

def point_datasets(request):
        #points = serialize('geojson', Incidences.objects.all())
        url = "http://10.0.3.23:1235/incidence_data/"
        response = urllib.request.urlopen(url)
        points = response.read()
        #return HttpResponse(data)
        return HttpResponse(points,content_type='json')

def retrieve_data(request):
        #import urllib
        url = "http://10.0.3.23:1235/farms/"
        response = urllib.request.urlopen(url)
        data = response.read()
        return HttpResponse(data)
