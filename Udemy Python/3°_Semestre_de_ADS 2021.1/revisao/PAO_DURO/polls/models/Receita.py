from django.db import models


class Receita(models.Model):
    id = models.IntegerField(primary_key=True, null=False, unique=True)
    nome = models.CharField(max_length=100)
    valores = models.DecimalField(max_digits=10, decimal_places=2)

    @staticmethod
    def calcular(valor):
        result = valor * 0.2

        return result
