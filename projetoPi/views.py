from rest_framework import viewsets
from projetoPi.models import ficha
from projetoPi.serializer import fichaSerializer

class fichasViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = ficha.objects.all()
    serializer_class = fichaSerializer