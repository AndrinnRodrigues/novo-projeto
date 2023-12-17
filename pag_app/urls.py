from django.urls import path
from pag_app import views

urlpatterns = [
    path('', views.home),
    path('salvar/', views.salvar, name="salvar"),
    path('api/deletar/<int:id>', views.deletar, name="deletar"),
    path('api/atualizar/<int:id>', views.atualizar, name="atualizar"),
    
    
    path('pesquisar/', views.pesquisar, name="pesquisar"),
    path('deletar/', views.pag_deletar, name="pag_deletar"),
    path('atualizar/', views.pag_atualizar, name="pag_atualizar"),
    path('criar/', views.pag_criar, name="pag_criar"),
    path('home/', views.home_2, name="pag_home"),      
]