from django.utils import timezone
from django.db import models

# Aqui vai ficar a classe modelo do Usuário
# Nome, sobrenome, cpf, telefone, email, foto, endereço.
# data_cadastro, ativo 
class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    endereco = models.CharField(max_length=100)
    data_cadastro = models.DateTimeField(default=timezone.now)
    ativo = models.BooleanField(default=True)
    

    def __str__(self):
        return f'{self.nome} {self.sobrenome}  '
# foto = 


# Filme - Nome do filme, ano de lançamento estúdio, gênero, sinopse, data de cadastro
    
#Gênero - nome, data de cadastro
    
class Filme(models.Model):
    nome_do_filme = models.CharField(max_length=50)
    ano_de_lancamento = models.DateField(default=timezone.now)
    estudio = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    sinopse = models.TextField()
    data_de_cadastro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome_do_filme

class Genero(models.Model):
    nome = models.CharField(max_length=50)
    data_de_cadastro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome