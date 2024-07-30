from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("",views.index, name="ShopHome"),
    path("about/",views.about, name="AboutUs"),
    

    path("notify/",views.notify, name="NotifyUs"),
    
    path("addcart/",views.addcart, name="AddCart"),
    
    path("items/<int:myid>",views.items, name="Items"),
    

    path("contact/",views.contact, name="contactUs"),

    path("tracker/",views.tracker, name="TrackingStatus"),
    
    path("search/",views.search, name="Search"),

    path("products/",views.productview, name="ProductSuccess"),
    
    path("checkout/",views.checkout, name="Chectout"),

    path('order/<int:myid>/', views.order, name='order'),
    # Handle form submission (product ID included as hidden field)
    path('order/', views.order, name='order_post'),

    
    path("shopitems/",views.shopitems, name="ShopNow"),
    
]
