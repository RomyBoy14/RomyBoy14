# C:\Users\RomyB14\Desktop\Projet_APG_Clean\APG\APG\urls.py

from django.contrib import admin
from django.urls import path, include

# Importations nécessaires pour servir les fichiers statiques et média en développement
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Inclut les URLs de votre application APG_app sous le préfixe 'apg/'
    path('apg/', include('APG_app.urls')),
]

# Cette partie est essentielle pour servir les fichiers statiques et média en mode développement.
# Elle ne doit être utilisée QUE lorsque DEBUG est à True.
# En production, un serveur web (comme Nginx ou Apache) servirait ces fichiers.
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Assurez-vous que MEDIA_URL et MEDIA_ROOT sont définis dans settings.py si vous utilisez MEDIA_URL ici
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
