from django.db import models

# Create your models here.

class Product(models.Model):

     # Define category choices
    CATEGORY_CHOICES = [
        ('Fullsleeves', 'fullsleeves'),
        ('Hoodie', 'hoodie'),
        ('T-shirts', 't-Shirt'),
        ('gift', 'gift'),
    ]

    SIZE_CHOICES_1ST = [
        ('M,', 'M'),
        ('L,', 'L'),
        ('XL,', 'XL'),
        ('XXL,', 'XXL'),
    ]
    

    SIZE_CHOICES_2ND = [
        ('M,', 'M'),
        ('L,', 'L'),
        ('XL,', 'XL'),
        ('XXL,', 'XXL'),
    ]
    
    
    SIZE_CHOICES_3RD = [
        ('M,', 'M'),
        ('L,', 'L'),
        ('XL,', 'XL'),
        ('XXL,', 'XXL'),
    ]
    
    SIZE_CHOICES_4TH = [
        ('M,', 'M'),
        ('L,', 'L'),
        ('XL,', 'XL'),
        ('XXL,', 'XXL'),
    ]

    OUT_OF_STOCK = [
        ('Out Of Stock', 'Out Of Stock'),
    ]

    
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='T-shirts')
    color =models.CharField(max_length=50, default="")


    outOfStock =models.CharField(max_length=50, default="",  blank=True,choices=OUT_OF_STOCK,)
    size =models.CharField(max_length=50, default="",  blank=True)
    size_1st =models.CharField(max_length=50, choices=SIZE_CHOICES_1ST, default="", blank=True )
    size_2nd =models.CharField(max_length=50,choices=SIZE_CHOICES_2ND, default="", blank=True)
    size_3rd =models.CharField(max_length=50, choices=SIZE_CHOICES_3RD, default="",blank=True)
    size_4th =models.CharField(max_length=50,choices=SIZE_CHOICES_4TH, default="", blank=True)
    
    discount =models.CharField(max_length=50, default="")
    
    price = models.IntegerField(null=True, blank=True)  # Allowing price to be empty
    image = models.ImageField(upload_to="shop/images" , default="")
    imageTwo = models.ImageField(upload_to="shop/images" , default="")
    desc = models.CharField(max_length=300)
    add_date = models.DateTimeField(auto_now_add=True)  # Automatically set to now when created

    # pub_date = models.DateField()

    def __str__(self) :
        return self.product_name


# creating contact module

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    option = models.CharField(max_length=50 ,default="")
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    phone =models.CharField(max_length=50, default="")
    desc =models.CharField(max_length=500, default="")
    

    # pub_date = models.DateField()

    def __str__(self) :
        return self.name


# creating contact module

class Order(models.Model):
    msg_id = models.AutoField(primary_key=True)
    allDesc = models.CharField(max_length=300, default="")
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    phone = models.CharField(max_length=15 , default="")
    alternate_phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255 ,default="")
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100 ,default="")
    state = models.CharField(max_length=100 , default="")
    pin = models.CharField(max_length=10 , default="")
    created_at = models.DateTimeField(auto_now_add=True)

    allSize =models.CharField(max_length=50, default="")
    imgPath = models.CharField(max_length=300, default="")

    def __str__(self):
        return f'{self.firstName} {self.lastName}'