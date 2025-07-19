# C:\Users\RomyB14\Desktop\Projet\APG_Clean\APG\APG_app\views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from datetime import datetime
import json

# Liste des produits agricoles disponibles (pour l'exemple)
PRODUCTS_LIST = [
    "Bananes plantains", "Haricots", "Choux", "Tomates",
    "Avocats greffés", "Avocats non greffés", "Poivrons", "Oignons",
    "Pommes de terre", "Arachides", "Maïs", "Manioc", "Ignames"
]

# Vue pour la page d'accueil
def home_view(request):
    context = {
        'message': 'Bienvenue sur APG (Agro Progressiste Group) !',
        'current_time': datetime.now().strftime("%H:%M:%S"),
    }
    return render(request, 'APG_app/home.html', context)

# Vue pour la page de connexion simplifiée
def login_view(request):
    if request.method == 'POST':
        contact_info = request.POST.get('contact_info', '').strip()
        if contact_info:
            # Ici, nous simulerons une connexion réussie en redirigeant l'utilisateur.
            # En production, il faudrait une VRAIE authentification (Django Auth, vérification email/numéro, etc.)
            request.session['user_contact'] = contact_info # Stocke l'info de contact dans la session
            return redirect('dashboard') # Redirige vers un tableau de bord ou la page d'accueil après "connexion"
        else:
            return render(request, 'APG_app/login.html', {'error_message': 'Veuillez entrer votre email ou numéro.'})
    return render(request, 'APG_app/login.html')

# Vue pour le tableau de bord (après connexion)
def dashboard_view(request):
    user_contact = request.session.get('user_contact', 'Invité')
    context = {
        'user_contact': user_contact,
    }
    return render(request, 'APG_app/dashboard.html', context) # Nouvelle page de tableau de bord

# Vue pour l'achat de produits
def acheter_produit_view(request):
    context = {
        'products': PRODUCTS_LIST,
        'user_contact': request.session.get('user_contact', 'Invité'),
        'payment_methods': ['Orange Money', 'MTN Mobile Money'],
    }
    return render(request, 'APG_app/acheter_produit.html', context)

# Vue pour commander/réserver un produit
def commander_reserver_view(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        contact_info = request.POST.get('contact_info')
        city = request.POST.get('city')
        delivery_date = request.POST.get('delivery_date')
        delivery_time = request.POST.get('delivery_time')
        action_type = request.POST.get('action_type') # 'commander' ou 'reserver'

        # Ici, vous traiteriez l'enregistrement de la commande/réservation dans une base de données.
        # Pour l'instant, nous affichons juste un message de confirmation.
        message = f"Votre demande de {action_type} pour '{product_name}' a été reçue. Nous vous contacterons au {contact_info} pour la livraison à {city} le {delivery_date} à {delivery_time}."
        return render(request, 'APG_app/commander_reserver.html', {'confirmation_message': message, 'products': PRODUCTS_LIST, 'user_contact': request.session.get('user_contact', 'Invité')})

    context = {
        'products': PRODUCTS_LIST,
        'user_contact': request.session.get('user_contact', 'Invité'),
    }
    return render(request, 'APG_app/commander_reserver.html', context)

# Vue pour vendre son produit
def vendre_produit_view(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        quantity = request.POST.get('quantity')
        contact_info = request.POST.get('contact_info')
        location = request.POST.get('location')

        # Traitez la demande de vente ici (ex: enregistrement dans DB, notification admin)
        message = f"Votre offre de vente pour '{quantity} de {product_name}' depuis {location} a été reçue. Nous vous contacterons au {contact_info}."
        return render(request, 'APG_app/vendre_produit.html', {'confirmation_message': message, 'user_contact': request.session.get('user_contact', 'Invité')})

    context = {
        'user_contact': request.session.get('user_contact', 'Invité'),
    }
    return render(request, 'APG_app/vendre_produit.html', context)

# Vue pour la formation à la carte
def formation_view(request):
    if request.method == 'POST':
        # Logique pour l'inscription ou la prise de rendez-vous
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        subject = request.POST.get('subject')
        message = f"Votre demande de formation pour '{subject}' a été reçue. Nous vous contacterons au {contact}."
        return render(request, 'APG_app/formation.html', {'confirmation_message': message, 'user_contact': request.session.get('user_contact', 'Invité')})

    context = {
        'user_contact': request.session.get('user_contact', 'Invité'),
    }
    return render(request, 'APG_app/formation.html', context)

# Vue pour les conseils d'expert
def conseils_expert_view(request):
    if request.method == 'POST':
        # Logique pour la prise de rendez-vous pour conseils
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        query = request.POST.get('query')
        message = f"Votre demande de conseil concernant '{query}' a été reçue. Nous vous contacterons au {contact}."
        return render(request, 'APG_app/conseils_expert.html', {'confirmation_message': message, 'user_contact': request.session.get('user_contact', 'Invité')})

    context = {
        'user_contact': request.session.get('user_contact', 'Invité'),
    }
    return render(request, 'APG_app/conseils_expert.html', context)

# Vue de déconnexion (très simple, juste pour vider la session)
def logout_view(request):
    if 'user_contact' in request.session:
        del request.session['user_contact']
    return redirect('home')
