from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from .models import books_taken,books_requested

# Create your views here.
def homepage(request):
	return render(request=request,
			template_name="web1/home.html",
			context={"context1":books_taken.objects.all,"context2":books_requested.objects.all})


def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("web1:homepage")


def login_request(request):
	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect('/')
			else:
				messages.error(request, "Invalid username or password.")
		else:
			messages.error(request, "Invalid username or password.")
	form = AuthenticationForm()
	return render(request = request,
				template_name = "web1/login.html",
				context={"form":form})