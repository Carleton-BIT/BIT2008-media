from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_task/', views.create_task, name='create_task'),
    path('accounts/', include('django.contrib.auth.urls')),
]