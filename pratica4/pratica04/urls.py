from django.urls import path
from .views import (
    EditoraList, EditoraCreate, EditoraUpdate, EditoraDelete, LivroList, LivroCreate, LivroUpdate, LivroDelete, AutorList, AutorCreate, AutorUpdate, AutorDelete, PublicaList, PublicaCreate, PublicaUpdate, PublicaDelete,
)

urlpatterns = [
    # URLs para o CRUD de Editora
    path('editoras/', EditoraList.as_view(), name='editora_list'),
    path('editoras/nova/', EditoraCreate.as_view(), name='editora_create'),
    path('editoras/<int:pk>/editar/', EditoraUpdate.as_view(), name='editora_update'),
    path('editoras/<int:pk>/deletar/', EditoraDelete.as_view(), name='editora_delete'),
    
    # URLs para Autor
    path('autores/', AutorList.as_view(), name='autor_list'),
    path('autores/novo/', AutorCreate.as_view(), name='autor_create'),
    path('autores/<int:pk>/editar/', AutorUpdate.as_view(), name='autor_update'),
    path('autores/<int:pk>/deletar/', AutorDelete.as_view(), name='autor_delete'),

    # URLs para Livro
    path('livros/', LivroList.as_view(), name='livro_list'),
    path('livros/novo/', LivroCreate.as_view(), name='livro_create'),
    path('livros/<int:pk>/editar/', LivroUpdate.as_view(), name='livro_update'),
    path('livros/<int:pk>/deletar/', LivroDelete.as_view(), name='livro_delete'),
    
    # URLs para Publica (Associações)
    path('publicacoes/', PublicaList.as_view(), name='publica_list'),
    path('publicacoes/nova/', PublicaCreate.as_view(), name='publica_create'),
    path('publicacoes/<int:pk>/editar/', PublicaUpdate.as_view(), name='publica_update'),
    path('publicacoes/<int:pk>/deletar/', PublicaDelete.as_view(), name='publica_delete'),
]

# **Não se esqueça** de incluir o `urls.py` do seu app no `urls.py` principal do projeto!