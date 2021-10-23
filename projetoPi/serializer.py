from rest_framework import serializers
from projetoPi.models import ficha

class fichaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ficha
        fields = '__all__'

     ##   fields = ['id', 'responsavel', 'produto', 'codigosemi_acabado', 'setor', 'diametrocabeca', 'diametrocorpofuro', 'alturatotal', 'divisao', 'passo', 'numerocarreira', 'gpm', 'pecasporminuto', 'tpe', 'pesobruto', 'pesoliquido', 'materialcodigo', 'espessuradafita', 'larguradafita']