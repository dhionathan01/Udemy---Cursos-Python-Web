from django.db import models


class Professor(models.Model):
    id = models.IntegerField(primary_key=True, null=False, unique=True)
    nome = models.CharField(max_length=50, null=False)
