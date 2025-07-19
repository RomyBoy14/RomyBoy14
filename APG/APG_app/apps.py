# C:\Users\RomyB14\Desktop\Projet\APG\APG_app\apps.py

from django.apps import AppConfig


class ApgAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'APG_app' # <-- TRÈS IMPORTANT : Doit être EXACTEMENT 'APG_app' (avec 'a' minuscule pour 'app')
