from django import forms
from .models import Editora, Autor, Livro, Publica

# 1. ModelForm para Editora
class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        # Inclui todos os campos do modelo (neste caso, apenas 'nome')
        fields = '__all__' 
        # Podemos adicionar classes CSS para estilização (ex: Bootstrap)
        # widgets = {
        #     'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da Editora'}),
        # }

# 2. ModelForm para Autor
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'
        # widgets = {
        #     'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Autor'}),
        # }

# 3. ModelForm para Livro
class LivroForm(forms.ModelForm):
    # Nota: O campo 'autores' é ManyToMany e, por padrão, o ModelForm 
    # cria um MultipleChoiceField (seleção múltipla).
    class Meta:
        model = Livro
        # Excluímos 'autores' por enquanto, pois o relacionamento Many-to-Many
        # via 'through' (Publica) é mais complexo em um único ModelForm.
        # Faremos a gestão dos autores separadamente com Publica.
        # Se não tivéssemos a 'through' table, '__all__' funcionaria.
        # fields = '__all__' # Não é o ideal neste cenário com 'through'
        
        fields = ['ISBN', 'titulo', 'publicacao', 'preco', 'estoque', 'editora']
        
        # Exemplo de customização de widgets
        #widgets = {
            #'publicacao': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            #'preco': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            #'estoque': forms.NumberInput(attrs={'class': 'form-control'}),
            # Editora (ForeignKey) será renderizada como um Select por padrão.
        #}

# 4. ModelForm para Publica (para gerenciar a associação Livro-Autor)
class PublicaForm(forms.ModelForm):
    class Meta:
        model = Publica
        # Note que precisamos dos campos 'livro' e 'autor'
        fields = '__all__'
        # widgets = {
        #     'livro': forms.Select(attrs={'class': 'form-select'}),
        #     'autor': forms.Select(attrs={'class': 'form-select'}),
        # }