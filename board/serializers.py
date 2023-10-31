from rest_framework import serializers
from .models import Board, Comments


class BoardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'

class BoardCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class CommentsShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
class BoardDetailSerializer(serializers.ModelSerializer):
    comments = CommentsShowSerializer(many=True)
    class Meta:
        model = Board
        fields = '__all__'