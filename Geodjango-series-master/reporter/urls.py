from django.conf.urls import include,url

from .views import HomePageView, county_datasets,point_datasets,wells_datasets,farms_datasets

urlpatterns = [
	url(r'^$', HomePageView.as_view(), name = 'home'),
	url(r'^county_data/$', county_datasets, name = 'county'),
	url(r'^incidence_data/$', point_datasets, name = 'incidences'),
        url(r'^wells/$', wells_datasets, name='wells'),
	url(r'^farms/$', farms_datasets, name='farms'),

]
