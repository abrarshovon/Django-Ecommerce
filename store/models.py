from django.db import models

# Create your models here.
class Promotion(models.Model):
    description= models.CharField(max_length=255)
    discount= models.FloatField()

class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product= models.ForeignKey('Product', on_delete=models.SET_NULL, null= True,related_name='+')

class Product (models.Model):
    title= models.CharField(max_length=255)
    description=models.TextField()
    price= models.DecimalField(max_digits=6, decimal_places=2)
    inventory= models.IntegerField()
    last_update=models.DateTimeField(auto_now=True)
    collection= models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotion= models.ManyToManyField(Promotion)

class Customer(models.Model):
    M_BRONZE = 'B'
    M_SILVER = 'S'
    M_GOLD = 'G'
    M_CHOICES=[
        (M_BRONZE,'Bronze'),
        (M_SILVER,'Silver'),
        (M_GOLD,'Gold'),

    ]
    first_name = models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    phone= models.CharField(max_length=255)
    birth_date=models.DateField(null=True)
    membership= models.CharField(max_length=1,choices=M_CHOICES, default=M_BRONZE)

class Order(models.Model):
    Pending = 'p'
    Complete = 'c'
    Failed = 'f'
    Payment_Status =[
        (Pending, 'pending'),
        (Complete, 'complete'),
        (Failed, 'failed')
    ]
    placed_at= models.DateTimeField(auto_now_add = True)
    payment = models.CharField(max_length=1, choices=Payment_Status, default=Pending)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.PROTECT)
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity= models.PositiveSmallIntegerField()
    unit_price=models.DecimalField(max_digits=6, decimal_places=2)

class Address(models.Model):
    street= models.CharField(max_length=255)
    city= models.CharField(max_length=255)
    customer=models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)

class Cart(models.Model):
    created = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart= models.ForeignKey(Cart, on_delete=models.CASCADE)
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField()

