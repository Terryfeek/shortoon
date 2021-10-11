from django.urls import path
from . import views

urlpatterns = [
    path('shortener', views.index, name = 'index'),
    path('create', views.create, name='create'),
    path('<str:pk>', views.go, name='go')
]