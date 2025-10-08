from django.db import models

class Editora(models.Model):
    # id INT (automático no Django)
    nome = models.CharField(max_length=100, unique=True) # unique=True para garantir unicidade

    def __str__(self):
        return self.nome

class Autor(models.Model):
    # id INT (automático no Django)
    nome = models.CharField(max_length=100, unique=True) # unique=True para garantir unicidade

    def __str__(self):
        return self.nome

class Livro(models.Model):
    # id INT (automático no Django)
    ISBN = models.CharField(max_length=13, unique=True) # unique=True para garantir unicidade
    titulo = models.CharField(max_length=200)
    publicacao = models.DateField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    estoque = models.IntegerField()
    # Editora_id_INT -> Relacionamento Muitos para Um (ForeignKey)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    # Relação Muitos para Muitos com Autor, usando o modelo 'Publica' como intermediário
    autores = models.ManyToManyField(Autor, through='Publica', related_name='livros')

    def __str__(self):
        return self.titulo

class Publica(models.Model):
    # Livro_id_INT e Autor_id_INT
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    class Meta:
        # Garante que um livro só pode ser associado a um autor uma única vez
        unique_together = ('livro', 'autor') 

    def __str__(self):
        return f"{self.livro.titulo} - {self.autor.nome}"