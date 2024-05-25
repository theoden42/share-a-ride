from .models import Profile
from rest_framework import generics
from .serializers import UserSerializer, ProfileSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model

User = get_user_model()


class SignUp(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class UserListApiView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_queryset(self):
        if str(self.kwargs['id']) == str(self.request.user.id):
            return Profile.objects.filter(user__id=self.kwargs['id'])
        else:
            return Profile.objects.filter(user__id=self.kwargs['id'])
