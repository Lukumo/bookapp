from .models import Category, Author, Book, Order
from django.contrib import admin

# Register your models here.
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Order)
