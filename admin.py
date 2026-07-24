from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'telefono', 'edad', 'email')
    search_fields = ('nombre', 'email')
    list_filter = ('edad',)