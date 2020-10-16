from django.contrib.auth import get_user_model

from rest_framework import generics, permissions
from mlhaiti.accounts.api.serializers import UserSerializer

User = get_user_model()

class UserCreateView(generics.CreateAPIView):
    permission_classes = []
    serializer_class = UserSerializer
    querysets = User.objects.all()
