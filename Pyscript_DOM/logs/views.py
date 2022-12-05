from django.shortcuts import render
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def index(request):
    return render(request, 'index.html')

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def index2(request):
    return render(request, 'index2.html')