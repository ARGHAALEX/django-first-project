from django.db import models

# Create your models here.
class Product(models.Model):
   product_id = models.AutoField
   product_name = models.CharField(max_length=50)
   catagory= models.CharField(max_length=50,default="")
   subcatagory= models.CharField(max_length=50,default="")
   price = models.IntegerField(default=0)
   image=models.ImageField(upload_to="shop/images",default="")
   desc = models.CharField(max_length=300)
   pub_date = models.DateField()

   def __str__(self):
      return self.product_name 