from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """This is a Data Transfer Object"""

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializing UserProfile"""

    class Meta:
        model = models.UserProfile
        fields = ('id','email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'},
            }
        }

    def create(self, validated_data):
        """Create new user"""
        user = models.UserProfile.objects.create_user(
            validated_data['email'],
            validated_data['name'],
            validated_data['password'],
        )

        return user

    def update(self, instance, validated_data):
        """update existing user"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
