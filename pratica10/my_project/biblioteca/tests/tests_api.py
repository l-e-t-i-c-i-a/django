from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Livro, Autor, Editora
from datetime import date
from django.contrib.auth.models import User, Group

class LivroAPITest(APITestCase):

    def setUp(self):
        # Criar dados iniciais para os testes de API
        self.autor = Autor.objects.create(nome="Autor Teste")
        self.editora = Editora.objects.create(nome="Companhia dos Testes")
        self.livro = Livro.objects.create(
            isbn="9999999999999",
            autor=self.autor,
            editora=self.editora,
            titulo="Teste",
            publicacao=date(2025, 10, 12),
            preco=29.90,
            estoque=10
        )
        # URL do endpoint de listagem/criação (ajuste conforme seu urls.py)
        self.url_list = reverse('api:livro-list') 

    def test_get_livros_list(self):
        """Verifica se a API retorna a lista de livros com sucesso (GET)"""
        response = self.client.get(self.url_list)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verifica se o título do livro criado no setUp está no JSON de resposta
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['titulo'], "Teste")

    def test_post_livro_create(self):
        # 1. Criar o grupo que a sua permissão IsAnalista exige
        grupo_analistas, _ = Group.objects.get_or_create(name='Analistas de Cadastro')
        
        # 2. Criar o usuário e adicioná-lo ao grupo
        user = User.objects.create_user(username='analista_user', password='password123')
        user.groups.add(grupo_analistas)
        
        # 3. Autenticar o usuário
        self.client.force_authenticate(user=user)

        """Verifica se a API permite criar um novo livro via POST"""
        dados = {
            "isbn": "1234567890123",
            "autor": self.autor.id,
            "editora": self.editora.id,
            "titulo": "A Revolução dos Bichos",
            "publicacao": "1945-08-17",
            "preco": "29.90",
            "estoque": 20
        }
        response = self.client.post(self.url_list, dados, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Livro.objects.count(), 2)

    def test_get_livro_detail(self):
        """Verifica se a API retorna os detalhes de um livro específico (GET/{id})"""
        url_detail = reverse('api:livro-detail', args=[self.livro.id])
        response = self.client.get(url_detail)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['isbn'], "9999999999999")