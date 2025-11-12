from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Autor, Editora, Livro
from .forms import AutorForm, EditoraForm, LivroForm
from django.shortcuts import render

def base_view(request):
    return render(request, 'biblioteca/base.html')

def dashboard(request):
    return render(request, 'biblioteca/dashboard.html')

# Mapeia entidade → (modelo, form)
MAPEAMENTO = {
    'autor': (Autor, AutorForm),
    'editora': (Editora, EditoraForm),
    'livro': (Livro, LivroForm),
}

def listar_objetos(request, entidade):
    modelo, _ = MAPEAMENTO.get(entidade, (None, None))
    if not modelo:
        return render(request, 'biblioteca/erro.html', {'mensagem': f'Entidade "{entidade}" inválida.'})
    # É uma boa prática ordenar antes de paginar
    objetos_list = modelo.objects.all().order_by('id')
    page_obj = None
    is_paginated = False

    # Aplica paginação apenas para a entidade 'livro'
    if entidade == 'livro':
        paginator = Paginator(objetos_list, 10) # 10 livros por página
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context_objetos = page_obj # O template irá iterar sobre 'page_obj'
        is_paginated = True
    else:
        context_objetos = objetos_list # Entidades sem paginação
    
    return render(request, 'biblioteca/lista.html', {
        'objetos': context_objetos, 
        'entidade': entidade,
        'is_paginated': is_paginated, # Flag para o template
        'page_obj': page_obj # Objeto Paginator para os controles
    })

def criar_objeto(request, entidade):
    _, Form = MAPEAMENTO.get(entidade, (None, None))
    if not Form:
        return render(request, 'biblioteca/erro.html', {'mensagem': f'Entidade "{entidade}" inválida.'})
    
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar', entidade=entidade)
    else:
        form = Form()

    return render(request, 'biblioteca/form.html', {'form': form, 'entidade': entidade})

def editar_objeto(request, entidade, pk):
    modelo, Form = MAPEAMENTO.get(entidade, (None, None))
    if not modelo:
        return render(request, 'biblioteca/erro.html', {'mensagem': f'Entidade "{entidade}" inválida.'})
    obj = get_object_or_404(modelo, pk=pk)
    if request.method == 'POST':
        form = Form(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('listar', entidade=entidade)
    else:
        form = Form(instance=obj)
    return render(request, 'biblioteca/form.html', {'form': form, 'entidade': entidade})

def deletar_objeto(request, entidade, pk):
    modelo, _ = MAPEAMENTO.get(entidade, (None, None))
    if not modelo:
        return render(request, 'biblioteca/erro.html', {'mensagem': f'Entidade "{entidade}" inválida.'})
    obj = get_object_or_404(modelo, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('listar', entidade=entidade)
    return render(request, 'biblioteca/confirmar_exclusao.html', {'objeto': obj, 'entidade': entidade})
