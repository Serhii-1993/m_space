from django.urls import path, include
from .views import UserRegisterView, UserDetailView, UserListView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/', UserListView.as_view(), name='user-list'),



]
