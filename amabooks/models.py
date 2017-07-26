from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
   class Meta:
       verbose_name_plural = "categories"
   name = models.CharField(max_length = 40)
   def __str__(self):
       return self.name

class Author(models.Model):
   fname = models.CharField(max_length = 100)
   lname = models.CharField(max_length = 100)
   email = models.EmailField(max_length = 600)
   def __str__(self):
        return self.fname

class Book(models.Model):
   name = models.CharField(max_length = 300)
   preface = models.TextField()
   image = models.ImageField(upload_to="staticfiles/img",null = True, blank = True)
   price = models.DecimalField(decimal_places=2, max_digits=10)
   author = models.ForeignKey(Author)
   categories = models.ManyToManyField(Category)
   available = models.BooleanField(default = True)
   def __str__(self):
        return self.name

class Order(models.Model):
   book = models.ForeignKey(Book)
   author = models.ForeignKey(Author)
