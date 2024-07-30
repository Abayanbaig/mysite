from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product, Contact, Order
from math import ceil

# Create your views here.
def index(request):
    # products = Product.objects.all()
    # print(products)

    allProds =[]
    catprods =Product.objects.values('category' , 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n=len(prod)
        nSlides =n//3 + ceil((n/3)+(n//3))
        allProds.append([prod,range(1,nSlides), nSlides])

    # params = {'no_of_slides':nSlides,'range': range(1,nSlides),'product':products
    params = {'allProds': allProds}
    return  render(request , 'shop/index.html', params)

def about(request):
    return render(request , 'shop/about.html')


def notify(request):
    
    #all oreders
    allOrders = Order.objects.all()
    
    order_reversed = list(allOrders[::-1])

    # all items
    contact = Contact.objects.all()
    contact_reversed = list(contact[::-1])
 
    params= {'allOrders':order_reversed , 'contact':contact_reversed }

    return render(request , 'shop/notify.html',params)

def addcart(request):

    # all items
    
    allitems = Product.objects.all()
    # n=len(allitems)
    # nSlides =n//3 + ceil((n/3)+(n//3))
    params = {'allitems':allitems }
    return render(request , 'shop/addcart.html' , params)


def items(request,myid):

    product = Product.objects.filter(id=myid)

    # all items
    
    allitems = Product.objects.all()
    # n=len(allitems)
    # nSlides =n//3 + ceil((n/3)+(n//3))
    params = {'allitems':allitems,'product':product[0] }
    return render(request , 'shop/all_items.html',params)

def contact(request):
    if request.method=="POST":
        print(request)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        
        option = request.POST.get('option', '')
        print(name , email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc , option=option)
        contact.save()
    return render(request , 'shop/contact.html')

def tracker(request):
    if request.method=="POST":
        print(request)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')

        option = request.POST.get('option', '')
        print(name , email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc, option=option)
        contact.save()
    return render(request , 'shop/tracker.html')

def search(request):
    return HttpResponse("we are about")

def productview(request):
    return render(request , 'shop/product.html' )

def checkout(request):
    return HttpResponse("we are about")



def order(request, myid):
    product = Product.objects.filter(id=myid)

    if request.method=="POST":
       # Extract form data from the POST request
       
       imgPath = request.POST.get('imgPath', '')
       allDesc = request.POST.get('allDesc', '')
       firstName = request.POST.get('firstName', '')
       lastName = request.POST.get('lastName', '')
       phone = request.POST.get('phone', '')
       alternate_phone = request.POST.get('alternate_phone', '')
       address = request.POST.get('address', '')
       address2 = request.POST.get('address2', '')
       city = request.POST.get('city', '')
       state = request.POST.get('state', '')
       pin = request.POST.get('pin', '')
       allSize = request.POST.get('allSize', '')
       print(firstName , lastName)

       order = Order(
            imgPath = imgPath ,
            allDesc = allDesc,
            firstName=firstName,
            lastName=lastName,
            phone=phone,
            alternate_phone=alternate_phone,
            address=address,
            address2=address2,
            city=city,
            state=state,
            pin=pin,
            allSize =allSize
            
            )
       order.save()
       # redirecting  page using name in urls
       return redirect('ProductSuccess')  

    params = {'product':product[0]}
    return render(request , 'shop/order.html', params)




def shopitems(request):
    allitems = Product.objects.all()
    # n=len(allitems)
    # nSlides =n//3 + ceil((n/3)+(n//3))
    params = {'allitems':allitems }
   
    
    return render(request , 'shop/shopItems.html', params)
# http://127.0.0.1:8000/