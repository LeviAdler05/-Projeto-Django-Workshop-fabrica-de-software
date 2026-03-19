from django.db import models

class Pessoa(models.Model):
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    localidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.logradouro}, {self.bairro}, {self.localidade}, {self.uf})"
    
