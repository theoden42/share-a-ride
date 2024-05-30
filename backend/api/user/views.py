from .models import Profile
from rest_framework import generics
from .serializers import ProfileSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model

User = get_user_model()


class SignUp(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class UserRetrieveApiView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
