from django.urls import path
from inicio import views
from .views import ServicesListView, ServiceDetailView, IncidenceDetailView, IncidencesListView 

inicio = 'inicio'


urlpatterns = [
    path('services/', ServicesListView.as_view(), name='service_list'),
    path('service/<int:pk>', ServiceDetailView.as_view(), name='service_detail'),
    path('incidences/', IncidencesListView.as_view(), name='incidence_list'),
    path('incidence/<int:pk>', IncidenceDetailView.as_view(), name='incidence_detail'),
]
