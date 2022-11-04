from rest_framework import serializers
from django.contrib.auth.models import User
from .models import work, accept, box

class userserializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username', 'password']
		extra_kwargs = {
			'password': {'write_only': True}
		}

	def create(self, validated_data):
		password = validated_data.pop('password', None)
		instance = self.Meta.model(**validated_data)
		if password is not None:
			instance.set_password(password)
		instance.save()
		return instance

class workserializer(serializers.ModelSerializer):
	class Meta:
		model = work
		fields = ['id', 'name', 'types', 'acces']

class acceptserializer(serializers.ModelSerializer):
	class Meta:
		model = accept
		fields = ['id','user', 'name', 'types', 'acces', 'done']



class boxserializer(serializers.ModelSerializer):
	class Meta:
		model = box
		fields = ['id', 'user', 'img', 'name', 'types', 'acces']
