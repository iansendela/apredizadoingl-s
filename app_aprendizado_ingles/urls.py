from app_aprendizado_ingles import views
from django.urls import path

urlpatterns = [
    path('adicionar_palavra/', views.adicionar_palavra, name='adicionar_palavra'),
    
    path('adicionar_frase/', views.adicionar_frase, name='adicionar_frase'),

    path('',views.pagina_inicial, name="home"), 

    path('todas_frases/', views.ver_frases, name='todas_frases'),

    path('frases_com_palavra/<int:palavra_id>/', views.frases_com_palavra, name='frases_com_palavra'),

    path('update_palavra/<int:palavra_id>/', views.update_palavra, name='update_palavra'),

    path('update_frase/<int:frase_id>/', views.update_frase, name='update_frase'),

    path('delete_frase/<int:frase_id>/', views.delete_frase, name='delete_frase'),

    path('todas_minhas_palavras/', views.todas_minhas_palavras, name='todas_minhas_palavras'),

    path('delete_palavra/<int:palavra_id>/', views.delete_palavra, name='delete_palavra'),

    path('todas_palavras_aprendidas/', views.todas_palavras_aprendidas, name='todas_palavras_aprendidas'),

    path('desmarcar_como_aprendida/<int:palavra_id>/', views.desmarcar_como_aprendida, name='desmarcar_como_aprendida'),

    path('desmarcar_frase_como_aprendida/<int:palavra_id>/', views.desmarcar_frase_como_aprendida, name='desmarcar_frase_como_aprendida'),

    path('desmarcar_conjugacoes_como_aprendida/<int:palavra_id>/', views.desmarcar_conjugacoes_como_aprendida, 
    name='desmarcar_conjugacoes_como_aprendida'),

    path('marcar_como_aprendida/<int:palavra_id>/', views.marcar_como_aprendida, name='marcar_como_aprendida'),

    path('marcar_frase_como_aprendida/<int:palavra_id>/', views.marcar_frase_como_aprendida, name='marcar_frase_como_aprendida'),

    path('marcar_como_aprendida/<int:palavra_id>/', views.marcar_conjugacoes_como_aprendida, name='marcar_conjugacoes_como_aprendida'),
]
