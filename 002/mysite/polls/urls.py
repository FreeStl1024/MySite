from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('', IndexView.as_view(), name='index'),
]