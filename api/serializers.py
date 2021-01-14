from rest_framework import serializers
from .models import Cat
from rest_framework.authtoken.models import Token

class PostSerializer(serializers.ModelSerializer):
    created_on = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    class Meta:
        model = Cat
        fields = ('id', 'created_on','details','detect') 


