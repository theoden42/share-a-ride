from django.urls import path
from api.ride import views
from .views import CreateRide, UpdateRide
urlpatterns = [
    path('', views.RideListAPIView.as_view()),
    path('filter/<str:src_loc>/<str:dst_loc>/',
         views.FilterRideListAPIView.as_view()),
    path('delete_ride/<int:id>/', views.DeleteRideAPIView.as_view()),
    path('create_ride/', CreateRide),
    path('update_ride/<int:id>/', UpdateRide),
]
