from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import models
from .forms import CreateUserForm, NewPostForm, NewBusinessForm, EditProfileForm, ChangeNeighborhoodForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def index(request):

    return render(request, 'neighborhood/index.html')

@login_required(login_url='login')
def feed(request):
    current_user = request.user.profile
    posts = models.Post.objects.filter(hood=current_user.neighborhood)

    if request.method == 'POST':
        new_post_form = NewPostForm(request.POST)
        if new_post_form.is_valid():
            new_post_form.instance.user = current_user
            new_post_form.instance.hood = current_user.neighborhood
            new_post_form.save()

            return redirect('feed')
    else:
        new_post_form = NewPostForm()

    title = 'Feed'
    context = {
        'title': title,
        'posts': posts,
        'new_post_form': new_post_form,
    }

    return render(request, 'neighborhood/feed.html',context)

@login_required(login_url='login')
def businesses(request):
    current_user = request.user.profile

    if request.method == 'POST':
        new_business_form = NewBusinessForm(request.POST)
        if new_business_form.is_valid():
            new_business_form.instance.user = current_user
            new_business_form.instance.neighborhood = current_user.neighborhood
            new_business_form.save()

            return redirect('businesses')
    else:
        new_business_form = NewBusinessForm()

    businesses = models.Business.objects.filter(neighborhood=current_user.neighborhood)

    title = 'Businesses'
    context = {
        'title': title,
        'businesses':businesses,
        'new_business_form':new_business_form,
    }

    return render(request, 'neighborhood/businesses.html', context)

@login_required(login_url='login')
def neighborhood(request):

    current_user = request.user
    neighborhood = current_user.profile.neighborhood

    
    
    title = 'Neighborhood'
    context = {
        'title': title,
        'neighborhood': neighborhood,
    }

    return render(request, 'neighborhood/neighborhood.html', context)

@login_required(login_url='login')
def profile(request):

    if request.method == 'POST':
        edit_profile_form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        change_neighborhood_form = ChangeNeighborhoodForm(request.POST, request.FILES, instance=request.user.profile)
        if edit_profile_form.is_valid():
            edit_profile_form.instance.user = request.user
            edit_profile_form.save()

            redirect('profile')
        elif change_neighborhood_form.is_valid():
            change_neighborhood_form.save()

            redirect('profile')

    else:
        edit_profile_form = EditProfileForm()
        change_neighborhood_form = ChangeNeighborhoodForm()

    title = 'Profile'
    context = {
        'title': title,
        'edit_profile_form': edit_profile_form,
        'change_neighborhood_form':change_neighborhood_form,
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
                nxt = request.GET.get("next", None)
                url = '/auth/login/'
                if nxt is not None:
                    url += '?next=' + nxt

                return redirect(url)

            else:
                messages.info(request, 'Username or password is incorrect.')
    title = 'Login'
    context = {'title':title}
    return render(request, 'auth/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('index')

