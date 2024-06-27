from rest_framework import generics
from .models import Ride, Passengers
from .serializer import RideSerializer, PassengerSerializer
from .permissions import IsRideOwner
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class RideListAPIView(generics.ListAPIView):
    "API view to list all rides"
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Ride.objects.all()
    serializer_class = RideSerializer


class FilterRideListAPIView(generics.ListAPIView):
    "API view to list rides from source to destination"
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = RideSerializer

    def get_queryset(self):
        # Access URL parameters
        query_src_location = self.kwargs['src_loc']
        query_dst_location = self.kwargs['dst_loc']

        queryset = Ride.objects.filter(
            src_location=query_src_location, dst_location=query_dst_location)
        if queryset is None:
            return "No such ride found"
        return queryset


class CreateRide(generics.CreateAPIView):
    serializer_class = RideSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class RetrieveUpdateRideView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsRideOwner, ]
    serializer_class = RideSerializer
    lookup_url_kwarg = 'id'
    queryset = Ride.objects.all()
    
class RetrieveUpdatePassengerView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsRideOwner]
    serializer_class = PassengerSerializer
    lookup_url_kwarg = 'id'
    queryset = Passengers.objects.all()
   
class CreateCoPassengers(generics.CreateAPIView):
    authentication_classes = JWTAuthentication
    permission_classes = IsAuthenticated
    serializer_class = PassengerSerializer
