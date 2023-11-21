from django.db import models

# Create your models here.

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    status = models.BooleanField()

    def __str__(self):
        return self.nome
    