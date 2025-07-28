# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import Comment, Todo
from .serializers import CommentSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

# Create Comment
class CommentCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, todo_id):
        todo = get_object_or_404(Todo, id=todo_id)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, todo=todo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# List Comments of a Todo
class CommentListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, todo_id):
        todo = get_object_or_404(Todo, id=todo_id)
        comments = todo.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


# Update a comment (only by owner)
class CommentUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        if comment.user != request.user:
            return Response({'detail': 'Not allowed'}, status=status.HTTP_403_FORBIDDEN)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Delete a comment (only by owner)
class CommentDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        if comment.user != request.user:
            return Response({'detail': 'Not allowed'}, status=status.HTTP_403_FORBIDDEN)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
