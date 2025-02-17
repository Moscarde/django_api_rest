from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Cadastro
from .serializer import CadastroSerializer


# Create your views here.
@api_view(http_method_names=["GET", "POST"])
def cadastros(request):
    if request.method == "GET":
        pessoa = Cadastro.objects.all()
        serializer = CadastroSerializer(pessoa, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = CadastroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
