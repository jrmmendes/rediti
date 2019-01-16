from django.urls import path
from .views import ProfileView, LogoutView, LoginView, SignupView

app_name = 'users'

urlpatterns = [
    path('<int:pk>/', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
]
