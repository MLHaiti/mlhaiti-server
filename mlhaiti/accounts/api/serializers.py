from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


from mlhaiti.accounts.models import Profile


class UserSerializer(serializers.ModelSerializer):
	def create(self, validated_data):
		user = User.objects.create_user(**validated_data)
		#Profile.objects.create(user=user)
		return user

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password']
		extra_kwargs = {"password":{"write_only": True}}
		validators = [
			UniqueTogetherValidator(
				queryset=User.objects.all(),
				fields=['username', 'email']
			)
		]
 