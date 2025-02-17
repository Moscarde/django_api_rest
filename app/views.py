from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Cadastro
from .serializer import CadastroSerializer


# Create your views here.
@api_view(http_method_names=["GET", "POST"])
def cadastros(request):
    if request.method == "GET":
        pessoas = Cadastro.objects.all()
        serializer = CadastroSerializer(pessoas, many=True)
        return Response({"cadastros": serializer.data})  # Melhor formato de retorno


    if request.method == "POST":
        serializer = CadastroSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"cadastro": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["GET", "PUT", "DELETE"])
def consulta_att_delete(request, id):
    try:
        cadastro = get_object_or_404(Cadastro, id=id)
    except ValueError:
        return Response({"error": "ID inválido"}, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "GET":
        serializer = CadastroSerializer(cadastro)
        return Response({"cadastro": serializer.data})

    elif request.method == "PUT":
        serializer = CadastroSerializer(cadastro, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"cadastro": serializer.data}, status=status.HTTP_200_OK)
        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        cadastro.delete()
        return Response(
            {"message": "Cadastro deletado com sucesso"},
            status=status.HTTP_204_NO_CONTENT,
        )
