# services/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path('', views.ServiceTypeList.as_view()),
    path('<int:pk>/', views.ServiceTypeDetail.as_view()),
    path('orders/', views.OrderList.as_view()),
    path('orders/<int:pk>/', views.OrderDetail.as_view()),

]


urlpatterns = format_suffix_patterns(urlpatterns)