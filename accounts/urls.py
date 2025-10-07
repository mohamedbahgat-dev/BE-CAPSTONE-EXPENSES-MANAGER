from django.urls import path
from .views import LogInView, SignUpView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', LogInView.as_view(), name='login' ),
    path('signup/', SignUpView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout')

]