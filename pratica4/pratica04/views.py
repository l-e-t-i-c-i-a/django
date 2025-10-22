from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Editora, Autor, Livro, Publica
from .forms import EditoraForm, AutorForm, LivroForm, PublicaForm

# CRUD para Editora (usando Class-Based Views - uma abordagem RAD/ágil)

# 1. Listar Editoras (Retrieve - R)
class EditoraList(ListView):
    model = Editora
    template_name = 'editora_list.html' # Criação posterior
    context_object_name = 'editoras'

# 2. Criar Nova Editora (Create - C)
class EditoraCreate(CreateView):
    model = Editora
    form_class = EditoraForm # Usa o ModelForm
    template_name = 'editora_form.html' # Formulário reutilizável para criação/edição
    success_url = reverse_lazy('editora_list') # Redireciona para a lista após sucesso

# 3. Atualizar Editora Existente (Update - U)
class EditoraUpdate(UpdateView):
    model = Editora
    form_class = EditoraForm
    template_name = 'editora_form.html'
    success_url = reverse_lazy('editora_list')

# 4. Deletar Editora (Delete - D)
class EditoraDelete(DeleteView):
    model = Editora
    template_name = 'editora_confirm_delete.html' # Confirmação de exclusão
    success_url = reverse_lazy('editora_list')

# -------------------------------------------------------------------
# CRUD para Autor
# -------------------------------------------------------------------

class AutorList(ListView):
    model = Autor
    template_name = 'autor_list.html'
    context_object_name = 'autores'

class AutorCreate(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'autor_form.html'
    success_url = reverse_lazy('autor_list')

class AutorUpdate(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'autor_form.html'
    success_url = reverse_lazy('autor_list')

class AutorDelete(DeleteView):
    model = Autor
    template_name = 'autor_confirm_delete.html'
    success_url = reverse_lazy('autor_list')

# -------------------------------------------------------------------
# CRUD para Livro
# -------------------------------------------------------------------

class LivroList(ListView):
    model = Livro
    template_name = 'livro_list.html'
    context_object_name = 'livros'

class LivroCreate(CreateView):
    model = Livro
    form_class = LivroForm
    template_name = 'livro_form.html'
    success_url = reverse_lazy('livro_list')

class LivroUpdate(UpdateView):
    model = Livro
    form_class = LivroForm
    template_name = 'livro_form.html'
    success_url = reverse_lazy('livro_list')

class LivroDelete(DeleteView):
    model = Livro
    template_name = 'livro_confirm_delete.html'
    success_url = reverse_lazy('livro_list')

# -------------------------------------------------------------------
# CRUD para Publica (Associação Livro-Autor)
# -------------------------------------------------------------------

class PublicaList(ListView):
    model = Publica
    template_name = 'publica_list.html'
    context_object_name = 'publicacoes'

class PublicaCreate(CreateView):
    model = Publica
    form_class = PublicaForm
    template_name = 'publica_form.html'
    success_url = reverse_lazy('publica_list')

class PublicaUpdate(UpdateView):
    model = Publica
    form_class = PublicaForm
    template_name = 'publica_form.html'
    success_url = reverse_lazy('publica_list')

class PublicaDelete(DeleteView):
    model = Publica
    template_name = 'publica_confirm_delete.html'
    success_url = reverse_lazy('publica_list')