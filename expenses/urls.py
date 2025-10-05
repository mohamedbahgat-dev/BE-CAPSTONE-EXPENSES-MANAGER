from django.urls import path
from .views import HomePageView, AddCategoryView

urlpatterns = [
    path('', HomePageView.as_view(), name='home' ),
    path('categories/add/', AddCategoryView.as_view(), name='add_category'),
    
]