from django.contrib import admin

from sistema import models

# Aqui fica o registro do Usuário
@admin.register(models.Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id','nome','sobrenome','email','ativo',)

#Aqui fica o registro do filme
@admin.register(models.Filme)
class Filme(admin.ModelAdmin):
    list_display = ('id','nome_do_filme','ano_de_lancamento','estudio','genero')

#Aqui fica o registro do Gênero   
@admin.register(models.Genero)
class Genero(admin.ModelAdmin):
    list_display = ('id','nome',)

