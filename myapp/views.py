from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': 'Неверное имя пользователя или пароль'})
    return render(request, 'login.html')

@login_required(login_url='login')  # защита от неавторизованных челиков
def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('login')
