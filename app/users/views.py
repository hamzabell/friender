from django.shortcuts import redirect, render
from django.contrib import messages
from .models import User
from django.contrib import auth
# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']


        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "you are now logged in")
            return redirect('index')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('login')

    return render(request, 'account/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        avatar = request.POST['avatar']
        last_name = request.POST['last_name']
        email = request.POST['email']
        date_of_birth = request.POST['date_of_birth']
        bio = request.POST['bio']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "That email being used")
            return redirect('register')

        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,
         date_of_birth=date_of_birth, password=password, bio=bio, avatar=avatar)
        user.save()

        messages.success(request, "User has been registered successfully")
        return redirect('login')

    return render(request, 'account/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out!')
        return redirect('index')

    return redirect('index')