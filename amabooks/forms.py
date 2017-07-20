from django import forms
from .models import Book

class RegisterForm(forms.Form):
    fname = forms.CharField(max_length = 100)
    lname = forms.CharField(max_length = 100)
    email = forms.EmailField(max_length = 600)
    password = forms.PasswordInput()
    confirm_password = forms.PasswordInput()



class LoginForm(forms.Form):
    fname = forms.CharField(max_length = 100)
    lname = forms.CharField(max_length = 100)
    password = forms.PasswordInput()


class BookForm(forms.Form):
    name = forms.CharField(max_length = 300)
    preface = forms.TextField()
    picture = forms.ImageField()
    price = forms.DecimalField(decimal_places=2, max_digits=10)
    author = forms.ForeignKey(Author)
    categories = forms.ManyToManyField(Category)
    available = forms.BooleanField(default = True)
