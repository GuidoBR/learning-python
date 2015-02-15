from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=50)
    foto = models.CharField(max_length=140)

    def __str__(self):
        return self.nome


class Shot(models.Model):
    titulo = models.CharField(max_length=140)
    imagem = models.CharField(max_length=200)
    conteudo = models.CharField(max_length=500)
    autor = models.ForeignKey(Autor)

    def __str__(self):
        return self.titulo + " - por " + str(self.autor)
