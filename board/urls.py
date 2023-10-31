from django.urls import path

from .views import BoardListView, BoardCreateView, BoardDetailView, CommentsAddView

urlpatterns = [
    path('', BoardListView.as_view(), name='board-list'),
    path('create/', BoardCreateView.as_view(), name='board-create'),
    path('<int:pk>/', BoardDetailView.as_view(), name='board-detail'),
    path('comments_add/', CommentsAddView.as_view(), name='comments-add')
]