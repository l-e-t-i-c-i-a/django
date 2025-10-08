from django.contrib import admin
from .models import Editora, Autor, Livro, Publica

# Registra os modelos
admin.site.register(Editora)
admin.site.register(Autor)
admin.site.register(Livro)
admin.site.register(Publica)