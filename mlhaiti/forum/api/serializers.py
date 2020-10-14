from rest_framework import serializers

from mlhaiti.index.serializers import UserSerializer

from .models import Forum, Message

import datetime

class MessageSerializer(serializers.ModelSerializer):
	created_by = UserSerializer(many=False, read_only=True)
	black_list_users = UserSerializer(many=True)
	class Meta:
		model = Message
		fields = ('id', 'date_created', 'is_deleted','content', 'created_by', 'black_list_users')

class ForumSerializer(serializers.ModelSerializer):
	created_by = UserSerializer(many=False, read_only=True)
	messages = MessageSerializer(many=True)
	class Meta:
		model = Forum
		fields = ('id', 'date_created', 'slug', 'subject', 'description', 'created_by', 'messages')