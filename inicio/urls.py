from django.urls import path
from inicio import views
from .views import ServicesListView, ServiceDetailView, IncidenceDetailView, IncidencesListView 

inicio = 'inicio'


urlpatterns = [
    path('', ServicesListView.as_view(), name='services'),
    path('service/<int:pk>', ServiceDetailView.as_view(), name='service'),
    path('incidences/', IncidencesListView.as_view(), name='incidences'),
    path('incidence/<int:pk>', IncidenceDetailView.as_view(), name='incidence_detail'),
]
