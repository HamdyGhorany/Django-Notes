from .models import Profile
from rest_framework import serializers
from django.contrib.auth.models import User

class JsonProfile(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class Json_User(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

