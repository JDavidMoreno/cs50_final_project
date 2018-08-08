from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'gotrees/index.html')

def register(request):

    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        first_name = request.POST["first_name"]


        user = User.objects.create_user(username, email, password, first_name=first_name)
        user.save()
        return HttpResponseRedirect(reverse('index'))


    else:
        return render(request, "gotrees/register.html")

def login_page(request):

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, "gotrees/login.html", {"message": "Sorry, your username or password is incorrect"})

    else:
        return render(request, "gotrees/login.html")


def logout_page(request):

    logout(request)
    return HttpResponseRedirect(reverse('index'))


def myforest(request, user_username):

    return render(request, "gotrees/myforest.html")


def edit_profile(request, user_username):


    if request.user.username == user_username:
        if request.method == 'POST':
            name = request.POST["name"]
            country = request.POST["country"]
            region = request.POST["region"]

            return HttpResponseRedirect(reverse('myforest'))
        else:
            return render(request, 'gotrees/edit_profile.html')

    else:
        return HttpResponseRedirect(reverse('index'))