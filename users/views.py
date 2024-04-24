from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def register_view(request):
    if request.user.is_authenticated:
        return HttpResponse(status=403, content="You are already registered")
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("posts:list")
    else:
        form = UserCreationForm()
        
    return render(request, 'auth/register.html', {
        "form": form,
    })


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponse(status=403, content="You are already logged in")
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect("dashboard:index")
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {
        "form": form,
    })


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return HttpResponse(status=405, content="Request Method Not Allowed")