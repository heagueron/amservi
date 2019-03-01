# services/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path('', views.api_root),
    path('orders/', views.OrderList.as_view(), name='order-list'),
    path('orders/<int:pk>/', views.OrderDetail.as_view(), name='order-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]


urlpatterns = format_suffix_patterns(urlpatterns)


# Added a URL at the empty string '' for api_root. 
# And since we’re using reverse (in services/views.py) 
# we also must add named urls to each existing view.