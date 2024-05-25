from .models import Profile
from rest_framework import generics 
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model

user = get_user_model()

class SignUp(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = Profile.objects.all()
    
class UserListApiView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = user.objects.all()
    def get_queryset(self):
        if self.kwargs['id'] == self.request.user.id:
            return user.objects.filter(id = self.request.user.id);
        else:
            return user.objects.filter(id = self.request.user.id).select_related('user_profile').defer('user_profile');
   #     # else:
    #     user.objects.all() 
    