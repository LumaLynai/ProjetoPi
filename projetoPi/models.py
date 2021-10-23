from django.db import models

class ficha(models.Model):
    responsavel = models.CharField(max_length=11)
    produto = models.CharField(max_length=11)
    codigosemi_acabado = models.CharField(max_length=11)
    setor = models.CharField(max_length=11)
    diametrocabeca = models.CharField(max_length=11)
    diametrocorpofuro = models.CharField(max_length=11)
    alturatotal = models.CharField(max_length=11)
    divisao = models.CharField(max_length=11)
    passo = models.CharField(max_length=30)
    numerocarreira = models.CharField(max_length=11)
    gpm = models.CharField(max_length=11)
    pecasporminuto = models.CharField(max_length=11)
    tpe = models.CharField(max_length=11)
    pesobruto = models.CharField(max_length=30)
    pesoliquido = models.CharField(max_length=9)
    materialcodigo = models.CharField(max_length=11)
    espessuradafita = models.CharField(max_length=11)
    larguradafita = models.CharField(max_length=11)

    def __str__(self):
        return self.responsavel
#adicionando mais funcionalidades depois