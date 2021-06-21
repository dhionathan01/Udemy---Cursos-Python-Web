from django.db import models


class Disciplina(models.Model):
    ID = models.IntegerField(primary_key=True, null=False, unique=True)
    nome = models.CharField(max_length=100)
    professor = models.ForeignKey('Professor', on_delete=models.CASCADE, null=False)
