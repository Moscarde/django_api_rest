from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Cadastro
from .serializer import CadastroSerializer

# Create your views here.
@api_view(http_method_names=["GET"])
def cadastros(request):
    pessoa = Cadastro.objects.all()
    serializer = CadastroSerializer(pessoa, many=True)
    return Response(serializer.data)