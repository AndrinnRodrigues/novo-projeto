from django.db import models

# Create your models here.
class Pessoa (models.Model):
    nome = models.CharField(max_length=150)
    data_nascimento = models.DateField(null=True, default=None)
    email = models.EmailField(max_length=150)
    pais = models.CharField(max_length=150)
   

    def __str__(self):
        return f"{self.nome}"
   