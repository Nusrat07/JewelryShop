from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.utils.text import slugify


from .models import Userprofile
from store.forms import ProductForm
from store.models import Product, Category

# Create your views here.

@login_required
def upload(request):
    return render(request,'userprofile/upload.html')


@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST,request.FILES)

        if form.is_valid():
            title = request.POST.get('title')
            product = form.save(commit=False)
            product.user = request.user
            product.slug = slugify(title)
            product.save()

            return redirect('upload')
    else:
        form = ProductForm()


    return render(request, 'userprofile/add_product.html', {'form':form})




@login_required
def myaccount(request):
    return render(request, 'userprofile/myaccount.html')


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)


        if form.is_valid():
            user = form.save()


            login(request, user)


            userprofile = Userprofile.objects.create(user=user)

            return redirect('frontpage')

    else:
        form = UserCreationForm()


    return render(request, 'userprofile/signup.html', {'form':form})
