from django.contrib import admin
from .models import cliente, pais, comida

# Se agrega en la vista admin la visualizacion de los 3 models.
admin.site.register(cliente)
admin.site.register(pais)
admin.site.register(comida)


