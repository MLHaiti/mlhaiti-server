from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from mlhaiti.index.models import Profile


class UserSerializer(serializers.ModelSerializer):
	def create(self, validated_data):
		user = User.objects.create_user(**validated_data)
		return user

	class Meta:
		model = User
		fields = ['id', 'username', 'first_name', 'email', 'last_name']


		validators = [
			UniqueTogetherValidator(
				queryset=User.objects.all(),
				fields=['username', 'email']
			)
		]