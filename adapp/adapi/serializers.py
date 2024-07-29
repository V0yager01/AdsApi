from rest_framework import serializers

from .models import Ad

from user.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Ad