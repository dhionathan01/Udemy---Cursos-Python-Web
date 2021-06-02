from django.db import models


class Venda(models.Model):
    ID = models.IntegerField(primary_key=True, null=False, unique=True)
    Date = models.DateTimeField()
    Valor = models.DecimalField(max_digits=10, decimal_places=2)
    departamento = models.ForeignKey('Departamento', on_delete=models.CASCADE, null=False)
