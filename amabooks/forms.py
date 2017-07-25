from django import forms
from .models import Book, Author, Category

class RegisterForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    password = forms.PasswordInput()
    confirm_password = forms.PasswordInput()



class LoginForm(forms.Form):
    full_name = forms.CharField()
    password = forms.PasswordInput()


class UploadForm(forms.Form):
    name = forms.CharField()
    preface = forms.CharField(widget = forms.Textarea)
    picture = forms.ImageField()
    price = forms.DecimalField(decimal_places=2, max_digits=10)
    author = forms.ModelChoiceField(queryset = Author.objects.all(), initial = 0)
    categories = forms.ModelMultipleChoiceField(queryset = Category.objects.all())
    available = forms.BooleanField()


class Order_bookForm(forms.Form):
    fname = forms.CharField()
    lname = forms.CharField()
    email = forms.EmailField()
    billing_address = forms.CharField()
