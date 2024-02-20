from django.urls import path
from inicio import views
from inicio.views import ServicesListView, ServiceDetailView, IncidenceListView, IncidenceDetailView


inicio = 'inicio'


urlpatterns = [
    path('services/', ServicesListView.as_view(), name='services_list'),
    path('services/', ServiceDetailView.as_view(), name='service_detail'),
    path('incidences/', IncidenceListView.as_view(), name='incidence_list'),
    path('incidences/', IncidenceDetailView.as_view(), name='incidence_detail'),
]
