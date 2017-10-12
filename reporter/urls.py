from django.conf.urls import include,url

from .views import PieChartView,HomePageView, BubbleView, county_datasets,point_datasets,wells_datasets,farms_datasets,retrieve_data

urlpatterns = [
	url(r'^$', HomePageView.as_view(), name = 'home'),
	url(r'^bubble/$', BubbleView.as_view(), name = 'bubble'),
	url(r'^county_data/$', county_datasets, name = 'county'),
	url(r'^incidence_data/$', point_datasets, name = 'incidences'),
	url(r'^pie_chart/$', PieChartView.as_view(), name=  'pie_chart'),
        url(r'^wells/$', wells_datasets, name='wells'),
	url(r'^farms/$', farms_datasets, name='farms'),
	url(r'^farms_map/$', retrieve_data, name='farms_map'),
]
