from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/home.html')


def create_post(request):
    return render(request, 'main/create_post.html')


def sign_up(request):
    return render(request, 'registration/sign_up.html')


def login(request):
    return render(request, 'registration/login.html')