from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import StudentProfile
from .serializers import UserSerializer, StudentProfileSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
