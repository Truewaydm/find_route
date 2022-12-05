from django.urls import path

# from travel.views import *
from cities.views import *
from cities.views import CityDetailView

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
]
