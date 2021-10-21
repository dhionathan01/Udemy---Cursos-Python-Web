from django.db import models


class Disciplina(models.Model):
    id = models.IntegerField(primary_key=True, null=False, unique=True)
    nome = models.CharField(max_length=100)
    periodo = models.IntegerField(null=False)
    dia_da_semana = models.CharField(max_length=20)
    hora_inicio = models.CharField(max_length=5)
    hora_fim = models.CharField(max_length=5)
    professor = models.ForeignKey('Professor', on_delete=models.CASCADE, null=False)