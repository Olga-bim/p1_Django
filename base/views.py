from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product



@api_view(['GET','POST', 'DELETE', 'PUT'])
def index(req):
    ar=[]
    for prod in Product.objects.all():
        ar.append({"desc":prod.desc, "price": prod.price})

    return Response(ar)

@api_view(['GET'])
def about(req):
    return Response('about')

@api_view(['GET'])
def test(req):
    return Response('test')