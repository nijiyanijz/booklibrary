from django.db import models
from django.contrib.auth.models import User
from owner.models import Books



#one to one relation-
#one to many relation-foreignkey
# class UserProfile(models.Model):
#     user=models.OneToOneField()
class Carts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    item=models.ForeignKey(Books,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    options=(
        ('incart','incart'),
        ('cancell','cancell'),
        ('order_palaced','order_placed')
    )
    status=models.CharField(max_length=120,choices=options,default='incart')

class Orders(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    item=models.ForeignKey(Books,on_delete=models.CASCADE)
    delivery_address=models.CharField(max_length=200)
    phone=models.CharField(max_length=15)
    date=models.DateField(auto_now_add=True)
    expected_delivery_date=models.DateField(null=True)
    options=(
        ('order_placed','order_placed'),
        ('dispatched','dispatched'),
        ('intransit','intransit'),
        ('delivered','delivered'),
        ('cancelled','cancelled')

    )
    status=models.CharField(max_length=50,choices=options,default='order_placed')


class Reviews(models.Model):
    item=models.ForeignKey(Books,on_delete=models.CASCADE,related_name='product')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='cust')
    review=models.TextField()
    options=(
        ('1','1'),
        ('1.5','1.5'),
        ('2', '2'),
        ('2.5', '2.5'),
        ('3', '3'),
        ('3.5', '3.5'),
        ('4', '4'),
        ('4.5', '4.5'),
        ('5', '5'),
    )
    rating=models.CharField(max_length=15,choices=options)



