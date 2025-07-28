from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import Project
from app.serializers import ProjectSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from app.permissions import IsProjectMember
from django.db.models import Q

# Create
class ProjectCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        projects = Project.objects.filter(
            Q(created_by=user) | Q(assigned_users=user)
        ).distinct()

        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

# Retrieve
class ProjectDetailView(APIView):
    permission_classes = [IsAuthenticated, IsProjectMember]
    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

# Update
class ProjectUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsProjectMember]
    def put(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete
class ProjectDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsProjectMember]
    def delete(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
