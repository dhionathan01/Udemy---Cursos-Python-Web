from django.db import models


class Departamento(models.Model):
    ID = models.IntegerField(primary_key=True, null=False, unique=True)
    nome = models.CharField(max_length=100)
    gerente = models.CharField(max_length=150)
    troco = models.DecimalField(max_digits=10, decimal_places=2)
    caixa = models.BooleanField()