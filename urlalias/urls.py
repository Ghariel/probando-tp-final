from django.urls import path

from . import views


urlpatterns = [
   
    path('api2', views.Api2.as_view(), name="api2"),
    path('<str:pk>', views.redir, name='redir'),#para redireccionar
    
   
]