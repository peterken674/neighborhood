from django.shortcuts import render


def index(request):

    return render(request, 'neighborhood/index.html')

def feed(request):

    return render(request, 'neighborhood/feed.html')

