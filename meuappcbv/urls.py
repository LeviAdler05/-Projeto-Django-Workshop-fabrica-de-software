from django.urls import path
from . import views


urlpatterns = [
    path('', views.ViaCepListView.as_view(), name='form'),
  
]