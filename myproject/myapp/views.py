# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.views.generic import TemplateView

def home(request):
    return render(request, 'home.html')

@login_required
def my_protected_view(request):
    # Your view logic here
    return render(request, 'registration/login.html')

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({'detail': 'Successfully logged in.'})
    return Response({'detail': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

class FrontendAppView(TemplateView):
    template_name = "index.html"

   

