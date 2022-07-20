from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def home(request):
    return render(request, 'main/home.html')


def create_post(request):
    return render(request, 'main/create_post.html')


def sign_up(request):
    # check if some form was posted
    if request.method == 'POST':
        # create the form with the posted information
        form = RegistrationForm(request.POST)

        if form.is_valid():
            # save the new user into the database
            user = form.save()
            # login the new user account
            login(request, user)

            return redirect('/home')

    else:
        form = RegistrationForm()

    return render(request, 'registration/sign_up.html', {'form': form})
