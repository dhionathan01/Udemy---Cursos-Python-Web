from django.db import models


class Professor(models.Model):
    ID = models.IntegerField(primary_key=True, null=False, unique=True)
    nome = models.CharField(max_length=100)
