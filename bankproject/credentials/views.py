from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def register_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            # Create a new user
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('login')  # Redirect to login page

    return render(request, 'register.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard page
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')
