from django.shortcuts import redirect, render
from shop.form import CustomUserForm
from .models import Category,Product
from django.contrib import messages

def home(request):
    products =Product.objects.filter(trending=1)
    return render(request,"shop/index.html",{"products":products})


def register(request):
    form=CustomUserForm()
    return render(request,"shop/register.html",{'form':form})

def collections(request):
    category=Category.objects.filter(status=0)
    return render(request,"shop/collection.html",{"category":category})
 

def collectionview(request,name):
    if(Category.objects.filter(name=name,status=0)):
        products=Product.objects.filter(category__name=name)
        return render(request,"shop/products/index.html",{"products":products,"category":name})
    else:
        messages.warning(request,"No Such Category found")
        return redirect('collection')

def product_Details(request,cname,pname):
    if(Category.objects.filter(name=cname,status=0)):
        if(Product.objects.filter(name=pname,status=0)):
            products=Product.objects.filter(name=pname,status=0).first()
            return render(request,"shop/products/product_Details.html",{"products":products})
        else:
            messages.error(request,"No Such Product Found")
            return redirect('collection') 
    else:
        messages.error(request,"No Such Category Found")
        return redirect('collection')