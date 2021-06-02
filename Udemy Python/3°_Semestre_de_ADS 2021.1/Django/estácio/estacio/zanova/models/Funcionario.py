from django.db import models


class Funcionario(models.Model):
    ID = models.IntegerField(primary_key=True, null=False, unique=True)
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=15)
    cargo = models.CharField(max_length=20)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = 30
    departamento = models.ForeignKey('Departamento', on_delete=models.CASCADE, null=False)
