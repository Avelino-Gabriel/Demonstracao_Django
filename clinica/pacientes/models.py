from django.db import models

# Create your models here.
class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome
