from django.shortcuts import render


def index(request):

    return render(request, 'neighborhood/index.html')

def feed(request):

    title = 'Feed'
    context = {
        'title': title,
    }

    return render(request, 'neighborhood/feed.html',context)

def businesses(request):

    title = 'Businesses'
    context = {
        'title': title,
    }

    return render(request, 'neighborhood/businesses.html', context)

def neighborhood(request):

    title = 'Neighborhood'
    context = {
        'title': title,
    }

    return render(request, 'neighborhood/neighborhood.html', context)

