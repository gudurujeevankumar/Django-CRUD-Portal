from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
def home(request):
    return render(request,'index.html')

def register(request):

    if request.method == 'POST':
        UserName = request.POST.get('UserName')
        FirstName = request.POST.get('FirstName')
        LastName = request.POST.get('LastName')
        Password = request.POST.get('Password')
        ConfirmPassword = request.POST.get('ConfirmPassword')

        # Password check
        if Password != ConfirmPassword:
            messages.error(request, "Passwords do not match!")
            return render(request, "register.html")

        # Username already exists
        if User.objects.filter(username=UserName).exists():
            messages.error(request, "Username already exists!")
            return render(request, "register.html")
        
        # Create user
        User.objects.create_user(
            username=UserName,
            first_name=FirstName,
            last_name=LastName,
            password=Password
        )
        messages.success(request, "Account created successfully!")
    return render(request, "register.html")

def login(request):

    if request.method == 'POST':

        UserName = request.POST.get('UserName')
        Password = request.POST.get('Password')

        user = authenticate(request, username=UserName, password=Password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Login successful!")
            next_page = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_page)

        else:
            messages.error(request, "Invalid username or password!")
            return render(request, "login.html")

    return render(request, "login.html")

def logout(request):
    auth_logout(request)
    messages.success(request, "You have been logged out successfully!")
    return redirect('login')