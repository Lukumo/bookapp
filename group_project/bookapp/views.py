from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from bookapp.models import Author, Books, Order, Category
from django.contrib.auth.models import User
from .forms import RegisterForm
from .forms import LoginForm
from .forms import BookForm
from .forms import OrderForm



def index(request):
    books = Books.objects.order_by('-date_created')
    categories = Category.objects.all()
    context = {"books": books,
               "categories": categories,
    }SSS
    return render(request, "bookapp/index.html", context)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            l=LoginForm
            l.fname = form.cleaned_data['fname']
            l.lname = form.cleaned_data['lname']
            l.password = form.cleaned_data['password']
            l.save()
            return HttpResponse('Hi' + l.fname)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            r = RegisterForm
            r.fname = form.cleaned_data['fname']
            r.lname= form.cleaned_data['lname']
            r.email= form.cleaned_data['email']
            r.password = form.cleaned_data['password']
            r.confirmpassword= form.cleaned_data['confirmpassword']
            r.save()
            return HttpResponse( 'welcome' +r.fname)
        else:
            return HttpResponse('invalid request')
    return redirect('index')


def authors(request):
    authors = Author.objects.all()
    context = { 'authors':authors

    }
    return render(request, 'book/authors.html', context)

def new_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            b= Books()
            b.name =form.cleaned_data['name']
            b.preface=form.cleaned_data['preface']
            b.price= form.cleaned_data['price']
            b.category_id= form.cleaned_data['category_id']
            b.author_id = form.cleaned_data['author_id']
            b.user= User.objects.get(pk = 1)
            b.save()
            return HttpResponse(b.name+' created')
        else:
           return HttpResponse ("invalid request")

    return redirect("index")

def order_book(request):
        if request.method == 'POST':
            form = BookForm(request.POST)
            if form.is_valid():
                o = Orders()
                o.book_id = form.cleaned_data['book_id']
                o.author_id = form.cleaned_data['author_id']
                o.save()
                return HttpResponse(o.name+' order successfull')
            else:
               return HttpResponse ("invalid request")

        return redirect("index")
from django.shortcuts import render

from django.contrib.auth.models import User
