from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'frontend/home.html', {

	})

def signinview(request):
	return render(request, 'frontend/signin.html', {

	})

def signupview(request):
	return render(request, 'frontend/signup.html', {

	})

def your(request):
	return render(request, 'frontend/your.html', {

	})

def explore(request):
	return render(request, 'frontend/explore.html', {

	})