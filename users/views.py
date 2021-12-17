from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("New User Account Created"))
            return redirect('index')
    else:
        register_form = RegisterForm()
        return render(request, 'register.html', {"register_form": register_form})
