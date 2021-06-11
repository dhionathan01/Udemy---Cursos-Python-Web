from django.db import models


class Avaliacao(models.Model):
    id = models.IntegerField(primary_key=True, null=False, unique=True)
    data = models.CharField(max_length=20)
    tipo_de_avaliacao = models.CharField(max_length=3)
    nota = models.DecimalField(max_digits=3, decimal_places=1)
    disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE, null=False)
