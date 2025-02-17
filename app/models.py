from django.db import models

# Create your models here.
class Cadastro(models.Model):
    nome = models.CharField(max_length=250)
    idade = models.IntegerField()
    data_cadastro = models.DateField(auto_now_add=True)
    