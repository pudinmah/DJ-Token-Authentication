from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response

# Create your views here.

@api_view(["POST"])
def signup(request):

    return Response({"message":"sign up page"})

@api_view(["POST"])
def login(request):

    return Response({"message":"login page"})

@api_view(["GET"])
def TestView(request):

    return Response({"message":"Test View page"})

@api_view(["POST"])
def logout(request):

    return Response({"message": "logout page"})