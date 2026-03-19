from django.urls import path
from . views import listar_pessoas, criar_pessoa, atualizar_pessoa, deletar_pessoa

urlpatterns = [
    path('listar/', listar_pessoas, name='listar_pessoas'),
    path('criar/', criar_pessoa, name='criar_pessoa'), 
    path('editar/<int:pk>', atualizar_pessoa, name='atualizar_pessoa'),
    path('deletar/<int:pk>', deletar_pessoa, name='deletar_pessoa'),

]