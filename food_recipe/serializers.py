from rest_framework import serializers
from .models import *

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipe
        fields=['id','title','description','instructions','ingredients','imgurl']

class SignupSerializer(serializers.Serializer):
    name=models.TextField(max_length=100)
    email=models.EmailField(primary_key=True)
    passwd=models.CharField()
    def create(self,validated_data):
        return Signup.objects.create(**validated_data)