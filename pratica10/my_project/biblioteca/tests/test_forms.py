from django.test import TestCase
from ..forms import AutorForm, SignUpForm
from django.contrib.auth import get_user_model

class FormTest(TestCase):

    def test_autor_form_valido(self):
        """Teste simples: Verifica se o formulário aceita dados corretos"""
        dados = {'nome': 'J.R.R. Tolkien'}
        form = AutorForm(data=dados)
        self.assertTrue(form.is_valid())

    def test_autor_form_invalido(self):
        """Verifica se o formulário rejeita nome vazio e se a classe CSS está presente"""
        form = AutorForm(data={'nome': ''})
        self.assertFalse(form.is_valid())
        # Verifica se o widget renderiza com a classe Bootstrap configurada
        self.assertIn('form-control', form.fields['nome'].widget.attrs['class'])

    def test_signup_email_duplicado(self):
        """Verifica a lógica customizada do clean_email no SignUpForm"""
        User = get_user_model()
        User.objects.create_user(username='existente', email='teste@email.com', password='123')
        
        # Tenta criar formulário com o mesmo e-mail
        dados = {
            'username': 'novo',
            'email': 'teste@email.com',
            'password1': 'senha123',
            'password2': 'senha123'
        }
        form = SignUpForm(data=dados)
        
        self.assertFalse(form.is_valid())
        self.assertIn('Este email já está em uso.', form.errors['email'])