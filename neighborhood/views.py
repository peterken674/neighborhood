from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib import messages


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

def profile(request):

    title = 'Profile'
    context = {
        'title': title,
    }

    return render(request, 'neighborhood/profile.html', context)

# AUTH
def register_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    else:
        form = CreateUserForm()
        title = 'New Account'

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')

    context = {'form': form, 'title': title}
    return render(request, 'auth/register.html', context)

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username or password is incorrect.')

    context = {}
    return render(request, 'auth/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('index')

