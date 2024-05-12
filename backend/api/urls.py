from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    # ride model urls to be added below
    # path("ride/", include(api.ride.urls)),
]
