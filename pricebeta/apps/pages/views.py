from django.shortcuts import render, redirect 
from django import forms
from django.contrib.auth.models import User

# importing shortcuts classes
from .forms import UserRegisterForm
# importing the user creation form created
class SignUpForm(UserRegisterForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2' )
        
# Create your views here.
# Defining the home/landing view
def home(request):
    return render(request, 'pages/index.html')

# defining the registration view
def register(request):
    # first creating an empty form
    form = SignUpForm
    # defining what to do when the form has being submitted
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login')

    else:
        form = SignUpForm()

    context = {
        'form': form
    }

    return render(request, 'pages/register.html', context)