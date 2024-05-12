from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path("admin/", admin.site.urls),
    # ride model urls to be added below
    # path("ride/", include(api.ride.urls)),
]
