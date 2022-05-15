from django.http import HttpResponse
from django.shortcuts import render
from listing.models import Band, Notification, Goodies  # add of the models create in models.py


def hello(request):  # config of the Hello page URL
    bands = Band.objects.all()  # input of all occurrence of the DB about Band() model
    notifications = Notification.objects.all()
    return render(request,  # here we input the request parameter about http request for render the pattern we want
                  'listing/hello.html',  # path since .\merchex\listing\templates\
                  {'bands': bands}  # add of the tag create upper
                  )

# the pattern is the same downer as the hello function


def about(request):
    return render(request,
                  'listing/about.html', )


def listings(request):
    Discs = Disc.objects.all()
    return render(request,
                  'listing/listings.html',
                  {'Discs': Discs},
                  )


def contact(request):
    return render(request,
                  'listing/contact.html', )
