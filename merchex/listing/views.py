from django.http import HttpResponse
from django.shortcuts import render
from listing.models import Band, Notification, Disc


def hello(request):
    bands = Band.objects.all()
    notifications = Notification.objects.all()
    return render(request,
                  'listing/hello.html',
                  {'bands': bands}
                  )


def about(request):
    return render(request,
                  'listing/about.html',)


def listings(request):
    Discs = Disc.objects.all()
    return render(request,
                  'listing/listings.html',
                  {'Discs': Discs},
                  )


def contact(request):
    return render(request,
                  'listing/contact.html',)
