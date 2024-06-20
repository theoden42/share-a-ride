from django.urls import path
from api.ride import views

urlpatterns = [
    path('', views.RideListAPIView.as_view()),
    path('filter/<str:src_loc>/<str:dst_loc>/',
         views.FilterRideListAPIView.as_view()),
    path('create_ride/', views.CreateRide.as_view()),
    path('<int:id>/', views.RetrieveUpdateDestroyRideView.as_view()),
]
