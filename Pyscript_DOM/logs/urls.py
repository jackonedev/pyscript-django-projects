from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index_view'),
    path('2/', views.index2, name='index2_view'),
]
