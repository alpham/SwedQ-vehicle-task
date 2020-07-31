from django.urls import path, include
from vehicles_demo.apps.vehicles import views


urlpatterns = [
    path('search/', views.search)
]
