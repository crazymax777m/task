from rest_framework import serializers
from .models import CustomUser, Car


class PersonSerializer(serializers.ModelSerializer):
    cars = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = CustomUser
        fields = ('name', 'email', 'language', 'cars',)


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('name',)
