from itertools import product
import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from shop.form import CustomUserForm
from .models import Cart, Category,Product,Favourite
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def home(request):
    products =Product.objects.filter(trending=1)
    return render(request,"shop/index.html",{"products":products})

def login_page(request):
    if request.method=='POST':
        name=request.POST.get('username')
        pwd=request.POST.get('password')
        user=authenticate(request,username=name,password=pwd)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged in Successfully")
            return redirect('home')
        else:
            messages.error(request,"Invalid User Name or Password")
            return redirect('login')
    return render(request,"shop/login.html")

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logout successfully")
    return redirect('login')

def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Success you can Login now..!")
            return redirect('login')
    return render(request,"shop/register.html",{'form':form})

def FavView(request):
    if request.user.is_authenticated:
      fav=Favourite.objects.filter(user=request.user)
      return render(request,"shop/favourite.html",{"fav":fav})
    else:
      return redirect("/")  

def remove_fav(request,fid):
    favitem=Favourite.objects.get(id=fid)
    favitem.delete()
    return redirect("/favourite")


def remove_cart(request,cid):
    cartitem=Cart.objects.get(id=cid)
    cartitem.delete()
    return redirect("/cart")

def add_to_cart(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_qty=data['product-qty']
            product_id =data['pid']
            product_status=Product.objects.get(id=product_id)
            if product_status:
                if Cart.objects.filter(user=request.user.id,product_id=product_id):
                    return JsonResponse({'status':'Product Already in Cart'}, status=200)
                else:
                    if product_status.qantity >=product_qty:
                        Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                        return JsonResponse({'status':'Product Added to Cart'},status=200)
                    else:
                        return JsonResponse({'status':'Product Stock Not Avaliable'},status=200)
        else:
            return JsonResponse({'status' :'Login to Add Cart'}, status=200)
    else:
        return JsonResponse({'status':'Invalid Access'},status=200)
    

def favourite(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_id =data['pid']
            product_status=Product.objects.get(id=product_id)
            if product_status:
                if Favourite.objects.filter(user=request.user.id,product_id=product_id):
                    return JsonResponse({'status' :'Product Already in Favourite'},status=200)
                else:
                    Favourite.objects.create(user=request.user,product_id=product_id)
                    return JsonResponse({'status' :'Product Added to Favourite'}, status=200)
        else:
            return JsonResponse({'status' :'Login to Add Cart'}, status=200)
    else:
        return JsonResponse({'status':'Invalid Access'},status=200)

def cart_page(request):
   if request.user.is_authenticated:
       cart=Cart.objects.filter(user=request.user) 
       return render(request,"shop/cart.html",{"cart":cart})
   else:
       return redirect("/")     

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