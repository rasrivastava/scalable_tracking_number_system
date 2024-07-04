from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_tracked_order, name='create_tracked_order'),
    path('track/<uuid:tracking_number>/', views.track_order, name='track_order'),
]
