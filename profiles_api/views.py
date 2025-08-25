from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import UserProfile
from .serializers import UserProfileSerializer



def index(request) -> HttpResponse:
    return render(request, "index.html")


@method_decorator(csrf_exempt, name='dispatch')
class UserProfilesView(APIView):
    """ Handle GET and POST for multiple users"""
    
    def get(self, request) -> Response:
        users = UserProfile.objects.all()
        serializer = UserProfileSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request) -> Response:
        
        many = isinstance(request.data, list)
        
        serializer = UserProfileSerializer(data=request.data, many=many)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class UserProfileView(APIView):
    """Handle GET, PUT, PATCH, DELETE for a single user"""

    def get(self, request, pk) -> Response:
        """Retrieve a user by ID"""
        user = get_object_or_404(UserProfile, pk=pk)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk) -> Response:
        """Update all fields of a user"""
        user = get_object_or_404(UserProfile, pk=pk)
        serializer = UserProfileSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk) -> Response:
        """Partially update user (only the fields you send)"""
        user = get_object_or_404(UserProfile, pk=pk)
        serializer = UserProfileSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk) -> Response:
        """Delete a user"""
        user = get_object_or_404(UserProfile, pk=pk)
        user.delete()
        return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

