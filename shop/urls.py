from django.urls import path
from .views import home,register,collections,collectionview,product_Details
urlpatterns=[
    path('home/',home,name="home"),
    path('register/',register,name="register"),
    path('collections/',collections,name="collection"),
    path('category/<str:name>/',collectionview,name="collection"),
    path('product/<str:cname>/<str:pname>/',product_Details,name="product_Details")
]