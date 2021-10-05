from django.urls import path
from django.urls.resolvers import URLPattern

from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
]
