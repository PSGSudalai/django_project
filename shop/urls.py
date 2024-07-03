from django.urls import path
from .views import home,register,collections,collectionview,product_Details,login_page,logout_page,add_to_cart,cart_page
urlpatterns=[
    path('home/',home,name="home"),
    path('login/',login_page,name="login"),
    path('logout/',logout_page,name="logout"),
    path('register/',register,name="register"),
    path('collections/',collections,name="collection"),
    path('category/<str:name>/',collectionview,name="collection"),
    path('product/<str:cname>/<str:pname>/',product_Details,name="product_Details"),
    path('add_to_cart/',add_to_cart,name="add_to_cart"),
    path('cart/',cart_page,name="cart"),

]