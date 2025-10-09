from django.urls import path
from .views import LogInView, SignUpView, ProfileView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', LogInView.as_view(), name='login' ),
    path('signup/', SignUpView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile' )

]