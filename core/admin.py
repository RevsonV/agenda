from django.contrib import admin
from core.models import Evento

# Register your models here.

"""
Para mostrar na tela da aplicação os campos desejados, usar o código conforme abaixo
"""

class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_evento', 'data_criacao')
    list_filter = ('usuario', 'data_evento',)

admin.site.register(Evento, EventoAdmin)
