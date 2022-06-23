from django.shortcuts import render
from .models import Demande

def index(request):
    return render(request, template_name="index.html")

def demande(request):
    demandes=Demande.objects.get(pk=1)
    nom='wafa'
    return render(request, template_name="demandes.html", context={"demandes":demandes,"nom":nom})

def nouvelle(request):
    return render(request, template_name="nouvelle.html")

def contact(request):
    return render(request, template_name="contact.html")

def connexion(request):
     return render(request, template_name="connexion.html")

def inscription(request):
     if request.method == "POST":
         return render(request, template_name="valide.html")
     else:
         return render(request, template_name="inscription.html")
