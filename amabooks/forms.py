from django import forms
from .models import Book, Author, Category,User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
   first_name = forms.CharField(max_length=30, required=False, help_text='Required.')
   last_name = forms.CharField(max_length=30, required=False, help_text='Required.')
   email = forms.EmailField(max_length=254, help_text='Required. Input a valid email address.')
   class Meta:
       model = User
       fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Book, Author, Category

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Input a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )



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
