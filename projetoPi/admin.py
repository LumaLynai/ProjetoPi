from django.contrib import admin
from projetoPi.models import ficha

class fichas(admin.ModelAdmin):
    list_display = ('id', 'responsavel', 'produto', 'codigosemi_acabado', 'setor', 'diametrocabeca', 'diametrocorpofuro', 'alturatotal', 'divisao', 'passo', 'numerocarreira', 'gpm', 'pecasporminuto', 'tpe', 'pesobruto', 'pesoliquido', 'materialcodigo', 'espessuradafita', 'larguradafita')
    list_display_links = ('id', 'responsavel')
    search_fields = ('nome',)
    list_per_page = 20


admin.site.register(ficha, fichas)
