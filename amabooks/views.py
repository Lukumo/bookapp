from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from amabooks.models import Author, Book, Order, Category
from .forms import RegisterForm
from .forms import LoginForm
from .forms import UploadForm
from .forms import Order_bookForm
# Create your views here.
def index(request):
    books = Book.objects.order_by('name')
    author = Author.objects.order_by("lname")
    categories = Category.objects.all()
    context = {"books": books,
               "categories": categories,
               "author":author
    }
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
        else:
            return HttpResponse('invalid request')
    return render(request, "bookapp/login.html")



def register(request):
    form = RegisterForm(request.POST)
    if request.method == 'POST':

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('bookapp/index.html')
        else:
            form = RegisterForm()
    return render(request, 'bookapp/registration.html', {'form': form})
    return redirect('bookapp/index.html')
    # form = RegisterForm(request.POST)
    # context = {"form" : form}
    # if request.method == 'POST':
    #     if form.is_valid():
    #         r = RegisterForm
    #         r.fname = form.cleaned_data['fname']
    #         r.lname= form.cleaned_data['lname']
    #         r.email= form.cleaned_data['email']
    #         r.password = form.cleaned_data['password']
    #         r.confirmpassword= form.cleaned_data['confirmpassword']
    #         r.save()
    #         return HttpResponse( 'welcome' +r.fname)
    #     else:
    #         return HttpResponse('invalid request')
    # return render(request, "bookapp/registration.html",context)



def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST)
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
            form = Order_bookForm(request.POST)
            if form.is_valid():
                o = Orders()
                o.book_id = form.cleaned_data['book_id']
                o.author_id = form.cleaned_data['author_id']
                o.save()
                return HttpResponse(o.name+' order successfull')
            else:
               return HttpResponse ("invalid request")

        return redirect("index")
