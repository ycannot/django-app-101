#from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import AppUser
from .serializers import AppUserSerializer
from django.shortcuts import get_object_or_404
from django.core import serializers


# Create your views here.

class AppuserSet(viewsets.ModelViewSet):
    serializer_class = AppUserSerializer
    queryset = AppUser.objects.all().order_by('username')

    #GET
    def list(self, request):
        #return Response('This is GET request')
        return Response(AppUserSerializer(self.queryset, many=True).data)

    #POST
    def create(self, request):
        data = self.save_and_parse_data(request)
        return Response("This is create request. user saved: "+str(data))

    def save_and_parse_data(self, request):
        #serializer = AppUserSerializer(data=request.data)
        #serializer.is_valid(raise_exception=True)
        #serializer.save()
        
        data = AppUser.objects.get(password = request.data["password"])
        #data = serializers.serialize('json', [ data, ])
        data = AppUserSerializer(data).data
        print("your POST data: ",data)
        
        return(data)