from django.test import TestCase
from ..models import Autor, Editora, Livro  # O ".." sobe um nível para achar o models.py
from datetime import date

class AutorModelTest(TestCase):
    def test_autor_str(self):
        autor = Autor.objects.create(nome="Machado de Assis")
        self.assertEqual(str(autor), "Machado de Assis")

# Você pode criar classes separadas para cada modelo para organizar melhor
class LivroModelTest(TestCase):
    def setUp(self):
        self.autor = Autor.objects.create(nome="Autor Teste")
        self.editora = Editora.objects.create(nome="Companhia dos Testes")

    def test_criacao_livro(self):
        livro = Livro.objects.create(
            isbn="9999999999999",
            autor=self.autor,
            editora=self.editora,
            titulo="Teste",
            publicacao=date(2025, 12, 10),
            preco=29.90,
            estoque=50
        )
        self.assertEqual(livro.titulo, "Teste")