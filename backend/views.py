from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Demande


def accueil(request):
    return render(request, template_name="accueil.html")

def index(request):
    if request.session.get("connected"):
        return HttpResponseRedirect(reverse('demandes'))
    else:
        return HttpResponseRedirect(reverse('connexion'))

def demande(request):
    if request.session.get("connected"):
        demandes=Demande.objects.all()
        nom='wafa'
        return render(request, template_name="demandes.html", context={"demandes":demandes,"nom":nom})
    else:
        return HttpResponseRedirect(reverse('connexion'))


def nouvelle(request):
    if request.session.get("connected"):
        return render(request, template_name="nouvelle.html")
    else:
        return HttpResponseRedirect(reverse('connexion'))

def contact(request):
    return render(request, template_name="contact.html")

def connexion(request):
     if request.method == "POST" :
         request.session["connected"] = True
         request.session["utilisateur"]="WAFA"
         return HttpResponseRedirect(reverse('demandes'))

     else:
         return render(request, template_name="connexion.html")

def deconnexion(request):
    request.session["connected"] = False
    return HttpResponseRedirect(reverse('connexion'))

def inscription(request):
     if request.method == "POST":
         return HttpResponseRedirect(reverse('demandes'))
     else:
         return render(request, template_name="inscription.html")
