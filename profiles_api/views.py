from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .models import ProfileFeedItem, UserProfile
from .serializers import ProfileFeedItemSerializer, UserProfileSerializer
from .permissions import UpdateOwnProfile, UpdateOwnStatus
from profiles_api import permissions



def index(request) -> HttpResponse:
    return render(request, "index.html")

class UserProfileViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing user profiles.
    """
    
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [UpdateOwnProfile]
    authentication_classes = [TokenAuthentication]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email']
    

class UserLoginAPIView(ObtainAuthToken):
    """ Handles User Authentication token"""
    
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    

class UserProfileFeedViewset(viewsets.ModelViewSet):
    """ Handles creating, reading and updating feed items """
    
    authentication_classes = [TokenAuthentication]
    serializer_class = ProfileFeedItemSerializer
    queryset = ProfileFeedItem.objects.all()
    permission_classes = [UpdateOwnStatus, IsAuthenticated]
    
    
    def perform_create(self, serializer):
        """ Sets the user profile to the logged in user"""
        
        serializer.save(user_profile=self.request.user)
       
    
