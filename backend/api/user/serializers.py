from django.db import IntegrityError
from rest_framework import serializers
from .models import Profile
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'id']
        extra_kwargs = {'username': {'validators': [UniqueValidator(queryset=User.objects.all())]}, 'password': {
            'write_only': True, 'required': True}, 'first_name': {'required': True}, 'last_name': {'required': True}}


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = '__all__'
        extra_kwargs = {'phone_number': {'required': True},
                        'user': {'required': True, 'read_only': True}, }

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        current_user = self.context['request'].user

        if (current_user.id != instance.user.id):
            representation.pop('phone_number')
        return representation

    def create(self, validated_data):
        user_data = validated_data.pop('user', None)
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)

        try:
            UserData = User.objects.create_user(
                **user_serializer.validated_data)
        except IntegrityError:
            raise serializers.ValidationError(
                {'username': 'This username is already taken.'})

        profile = Profile.objects.create(user=UserData, **validated_data)
        return profile
