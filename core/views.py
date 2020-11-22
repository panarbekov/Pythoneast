from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout


def homepage(request):
    return render(request, "core/index.html")


def authorization(request):
    if request.method == 'POST':
        form = request.POST
        user_login = form["login"]
        password = form["password"]
        user = User.objects.get(username=user_login)
        if user.check_password(password):
            login(request, user)
            return redirect(homepage)

    return render(request, "core/login.html")


def signout(request):
    logout(request)
    return redirect(homepage)


def registration(request):
    if request.method == 'POST':
        login = request.POST.get("login")
        password_1 = request.POST.get("password1")
        password_2 = request.POST.get("password2")
        if User.objects.filter(username=login).exists():
            return render(request, "core/registration.html")
        elif password_1 != password_2:
            return render(request, "core/registration.html")
        else:
            new_user = User()
            new_user.username = login
            new_user.set_password(password_1)
            new_user.save()
            return redirect(authorization)
    return render(request, "core/registration.html")

# Create your views here.
 