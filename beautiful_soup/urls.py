from django.urls import path
from . import views

urlpatterns = [
    path('', views.scrape, name='beautiful_soup_index'),
    path('delete/', views.delete, name='beautiful_soup_delete'),
]