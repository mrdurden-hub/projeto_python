from django.contrib import admin
from . models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone',
                    'email', 'categoria', 'data_criacao', 'mostrar')
    list_display_links = ('id', 'nome', 'sobrenome',)
    #list_filter = ('nome', 'sobrenome')
    list_per_page = 10
    search_fields = 'nome', 'sobrenome', 'telefone', 'id'
    list_editable = ('telefone', 'mostrar')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
