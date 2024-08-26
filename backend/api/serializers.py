from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Interview

# creating a serializer - helps communicate with the db using json data
# serializer takes python object and converts into json data and vice versa

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}} # only password write is possible, not read

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data) # validated data is data that passes all checks from the serializer
        return user

class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = ["id", "title", "role", "questions", "answers", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}