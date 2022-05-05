from django.http import HttpResponse
from django.shortcuts import render
from listing.models import Band


def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
    <h1>Hello Django ! </h1>
    <p>Mes groupes préféres sont :<p>
    <ul>
        <li>{bands[0].name}</li>
        <li>{bands[1].name}</li>
        <li>{bands[2].name}</li>
    </ul>
""")


def about(request):
    return HttpResponse('<h1>à propos</h1> <p>Nous adorons merch!</p>')


def listings(request):
    return HttpResponse('<h1>Dernières Annonces pour les articles</h1> <p>MrYéyé - Chrysalide -> vendu</p>')


def contact(request):
    return HttpResponse('<h1>Formulaire de contact</h1> <p>Entrez vos coordonnées ci dessous nous vous contacterons '
                        'prochainement</p>')
