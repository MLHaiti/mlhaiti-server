from django.shortcuts import render

from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from rest_framework.status import (
	HTTP_401_UNAUTHORIZED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_403_FORBIDDEN,
)

from mlhaiti.forum.serializers import ForumSerializer 
from mlhaiti.index.serializers import UserSerializer 
from mlhaiti.forum.models import Forum 

class UserList(generics.ListAPIView):
	permission_classes = (permissions.AllowAny,)
	queryset = User.objects.all()
	serializer_class = UserSerializer

class ForumList(generics.ListAPIView):
	permission_classes = (permissions.AllowAny,)
	queryset = Forum.objects.all()
	serializer_class = ForumSerializer
	model = serializer_class.Meta.model
	paginate_by = 1

	def list(self, request):
		queryset = self.get_queryset()
		forum_serializer = ForumSerializer(queryset, many=True)
		return Response({'error':False, "message": "success", "result":forum_serializer.data, "code": 200}, status=HTTP_200_OK)
