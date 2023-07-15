from django.urls import path, include

from .views import *


urlpatterns= [
  
  path( '',Home.as_view(), name='home'),
  path( 'customer/',Customer.as_view(), name='cust-page'),
  path('', views.property_list, name='property_list'),
  path('property/<int:property_id>/', views.property_detail, name='property_detail'),
  path('property/submit/', views.property_submit, name='property_submit'),
]
