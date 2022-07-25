from django.shortcuts import render, redirect 
from django import forms
from django.contrib.auth.models import User
from apps.pages.models import Category,Product,WishList
from django.views import View
# importing shortcuts classes
from .forms import UserRegisterForm
# importing the user creation form created
class SignUpForm(UserRegisterForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2' )
    
    # to get a users emails in case of mass emailing, and for other stuff involving the email,
    @staticmethod
    def get_User_by_email(email):
        try:
            return User.objects.get(email=email)
        except:
            return False   
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


def products(request):
    product = Product.objects.all()
    context = {
        'product': product
    }
    return render(request,'pages/products.html', context)

def categories(request):
    category=Category.objects.all()
    context= {
        'category': category
    }
    return render(request, 'pages/products.html', context)