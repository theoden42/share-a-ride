from rest_framework import generics
from .models import Ride
from .serializer import RideSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


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

        queryset = Ride.objects.filter(
            src_location=query_src_location, dst_location=query_dst_location)
        return queryset


class DeleteRideAPIView(generics.DestroyAPIView):
    "API view to delete a particular ride"
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    lookup_url_kwarg = 'id'
    print(id)


@csrf_exempt
def CreateRide(request):
    "API view to create a new ride"
    if request.method == "POST":
        ride_data = JSONParser().parse(request)
        serializer = RideSerializer(data=ride_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    return JsonResponse({"error": "wrong HTTP request"}, status=406)


@csrf_exempt
def UpdateRide(request, id):
    "API view to update no of passengers"
    if request.method == "POST":
        ride_data = get_object_or_404(Ride, id=id)
        data = JSONParser().parse(request)
        updated_passengers = data.get('num_passengers')
        if updated_passengers is not None:
            serializer = RideSerializer(ride_data, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        return JsonResponse({"error": "wrong field update request"}, status=404)
    return JsonResponse({"error": "wrong HTTP request"}, status=406)
