from django.urls import path
from api.user import views
urlpatterns = [
    path('signup/', views.SignUp.as_view()),
    path('profile/<int:id>/', views.UserListApiView.as_view()),
    # path('login',views.Login.as_view()),
]
