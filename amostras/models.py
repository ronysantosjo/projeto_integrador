from django.db import models

# Create your models here.

class Amostra(models.Model):
    data_recebimento = models.DateField()
    nome_amostra = models.TextField()
    data_liberacao = models.DateField()
    exame_direto = models.TextField()
    metodo_sheaters = models.TextField()
