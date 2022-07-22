from django.shortcuts import render, redirect 
# importing shortcuts classes
from .forms import UserRegisterForm
# importing the user creation form created

# Create your views here.
# Defining the home/landing view
def home(request):
    return render(request, 'pages/index.html')

# defining the registration view
def register(request):
    # first creating an empty form
    form = UserRegisterForm
    # defining what to do when the form has being submitted
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login')

    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }

    return render(request, 'pages/register.html', context)