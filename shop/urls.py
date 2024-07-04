from django.urls import path
from .views import home,register,collections,collectionview,product_Details,login_page,logout_page,add_to_cart,cart_page,remove_cart,favourite,FavView,remove_fav
urlpatterns=[
    path('home/',home,name="home"),
    path('login/',login_page,name="login"),
    path('logout/',logout_page,name="logout"),
    path('register/',register,name="register"),
    path('remove_cart/<str:cid>/',remove_cart,name="remove_cart"),
    path('collections/',collections,name="collection"),
    path('category/<str:name>/',collectionview,name="category"),
    path('product/<str:cname>/<str:pname>/',product_Details,name="product_Details"),
    path('add_to_cart/',add_to_cart,name="add_to_cart"),
    path('cart/',cart_page,name="cart"),
    path('favourite/',favourite,name="favourite"),
    path('favView/',FavView,name="favView"),
    path('remove_fav/<int:fid>/',remove_fav,name="remove_fav"),

]