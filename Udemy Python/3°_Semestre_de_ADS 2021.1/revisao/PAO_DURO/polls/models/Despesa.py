from django.db import models


class Despesa(models.Model):
    id = models.IntegerField(primary_key=True, null=False, unique=True)
    nome = models.CharField(max_length=100)
    gastos = models.DecimalField(max_digits=10, decimal_places=2)
