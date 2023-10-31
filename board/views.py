from django.shortcuts import render
from rest_framework import generics
from .models import Board, Comments
from .serializers import BoardListSerializer, BoardCreateSerializer, BoardDetailSerializer, CommentsShowSerializer

class BoardListView(generics.ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardListSerializer

class BoardCreateView(generics.CreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardCreateSerializer

class BoardDetailView(generics.RetrieveAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardDetailSerializer

class CommentsAddView(generics.CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsShowSerializer