from django.db import models


class Books(models.Model):
 book_name=models.CharField(max_length=120,unique=True)
 author=models.CharField(max_length=120)
 price=models.PositiveIntegerField()
 copies=models.PositiveIntegerField()
 published_date=models.DateField(null=True)
 image=models.ImageField(upload_to='images',null=True)

 def __str__(self):
  return self.book_name    #booknmae print cheyum





