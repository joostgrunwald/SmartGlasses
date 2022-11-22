from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if (form.is_valid()):
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("login:homepage")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request = request, template_name = "login/login.html", context={"login_form":form})
    
def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("login:homepage")

def homepage(request):
    return render(request = request, template_name = "login/home.html")
