from django.urls import path
from . import views


urlpatterns = [
    path('', views.ServiceTypeListCreate.as_view() ),
]