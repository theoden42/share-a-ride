from rest_framework import generics
from .models import Ride
from .serializer import RideSerializer

class RideListAPIView(generics.ListAPIView):
    "API view to list all rides"
    queryset = Ride.objects.all()
    serializer_class = RideSerializer

class FilterRideListAPIView(generics.ListAPIView):
    "API view to list rides from source to destination"
    serializer_class = RideSerializer
    
    def get_queryset(self):
        # Access URL parameters
        query_src_location = self.kwargs['src_loc']
        query_dst_location = self.kwargs['dst_loc']

        queryset = Ride.objects.filter(src_location=query_src_location, dst_location=query_dst_location)
        return queryset

    
        






      
        

