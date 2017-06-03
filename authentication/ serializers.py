from rest_framework import serializers
from .models import Users

class UsersListSerializer(serializers.ModelSerializer):
	class Meta:
		model=Users
		fields=('username','first_name','email')

class UserUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model=Users
		fields=('first_name','last_name','email')