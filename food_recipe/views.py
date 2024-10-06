from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
import io
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class RecipeListCreate(generics.ListCreateAPIView):
    queryset=Recipe.objects.all()
    serializer_class=RecipeSerializer

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Recipe.objects.all()
    serializer_class=RecipeSerializer

@csrf_exempt
def user_create(request):
    if request.method=='POST':
        json_data=request.body
        stream = io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer= SignupSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Saved'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')        