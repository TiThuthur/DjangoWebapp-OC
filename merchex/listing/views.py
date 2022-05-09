from django.http import HttpResponse
from django.shortcuts import render
from listing.models import Band, Notification


def hello(request):
    bands = Band.objects.all()
    notifications = Notification.objects.all()
    return render(request,
                  'listing/hello.html',
                  {'bands': bands}
                  )


def about(request):
    return HttpResponse('<h1>à propos</h1> <p>Nous adorons merch!</p>')


def listings(request):
    return HttpResponse('<h1>Dernières Annonces pour les articles</h1> <p>MrYéyé - Chrysalide -> vendu</p>')


def contact(request):
    return HttpResponse('<h1>Formulaire de contact</h1> <p>Entrez vos coordonnées ci dessous nous vous contacterons '
                        'prochainement</p>')
