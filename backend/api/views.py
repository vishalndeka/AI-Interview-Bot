from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, InterviewSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Interview
# Create your views here.

# generics.createAPIView is an already available class that handles creating new user
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer # this tells what kind of data to accept to make a user i.e. UserSerializer class
    permission_classes = [AllowAny]

# creating an interview
class InterviewListCreate(generics.ListCreateAPIView):
    serializer_class = InterviewSerializer
    permission_classes = [IsAuthenticated]

    # this method returns all interviews created by the particular user
    def get_queryset(self):
        user = self.request.user
        return Interview.objects.filter(author=user)
    
    # overriding create method, for custom functionality - checking if all fields are valid, right datatype, under character limit etc
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

# view to delete an interview
class InterviewDelete(generics.DestroyAPIView):
    serializer_class = InterviewSerializer
    permission_classes = [IsAuthenticated]

    # can onl;y delete your interview
    def get_queryset(self):
        user = self.request.user
        return Interview.objects.filter(author=user)
    
