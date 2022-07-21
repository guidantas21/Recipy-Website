from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# this class extends the UserCreationForm
class RegistrationForm(UserCreationForm):
    # rewriting the email form to be required, not optional 
    email = forms.EmailField(required=True)

    class Meta:
        # indicating the user model
        model = User
        # passing the prebuilt fields 
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']