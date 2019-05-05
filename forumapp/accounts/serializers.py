from rest_framework import serializers
from django.contrib.auth.models import User
from knox.models import AuthToken
from django.contrib.auth import authenticate
from forum.models import Profile


class ProfileSerializer2(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('bio', 'location', 'avatar')


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    profil = ProfileSerializer2()

    class Meta:
        model = User
        fields = ('id', 'username', 'profil')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

# Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")