# C:\Users\RomyB14\Desktop\Projet_APG_Clean\APG\APG_app\urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'), # Nouvelle page après connexion
    path('acheter/', views.acheter_produit_view, name='acheter_produit'),
    path('commander-reserver/', views.commander_reserver_view, name='commander_reserver'),
    path('vendre/', views.vendre_produit_view, name='vendre_produit'),
    path('formation/', views.formation_view, name='formation'),
    path('conseils-expert/', views.conseils_expert_view, name='conseils_expert'),
    path('logout/', views.logout_view, name='logout'), # Nouvelle route de déconnexion
]
