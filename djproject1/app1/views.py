from django.shortcuts import render
from django.views import generic
from app1.models import Book, Author, BookInstance, Genre, bookSerializer
from django.shortcuts import get_object_or_404

from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from logpipe import Producer
# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()
    # Number of visits to this view, as counted in the session variable.
    num1_vizits = request.session.get('num1_vizits',0)
    request.session['num1_vizits'] = num1_vizits + 1
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num1_vizits' : num1_vizits,




    }
# Render the HTML template index.html with the data in the context variable
    return render(request, 'app1/index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    context_object_name = 'book_list'   # your own name for the list as a template variable
    queryset = Book.objects.all()
    template_name = 'app1/book_list.html'  # Specify your own template name/location

class BookDetailView(generic.DetailView):
    model = Book
    def book_detail_view(request, primary_key):
    	book = get_object_or_404(Book, pk=primary_key)
    	return render(request, 'app1/book_detail.html', context={'book': book})

class AuthorListView(generic.ListView):
 	model = Author
 	paginate_by = 10
 	context_object_name = 'author_list'
 	queryset = Author.objects.all()
 	template_name = 'app1/authors_list.html'

class AuthorDetailView(generic.DetailView):
	model = Author
	def author_detail_view(request, primary_key):
		author = get_object_or_404(Author, pk=primary_key)
		return render(request, 'app1/author_detail.html',context = {'author': author})


#sign up page

"""def signup(request):
	form = UserCreationForm(request.POST)
	if form.is_valid():
		form.save()
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username = username,password = password)
		login(request,user)
	return render(request,"app1/signup.html",{'form':form})
def process(request):
	return HttpResponse('<h1> u r gae lmao </h1>')
def logged(request):
	return HttpResponse('<h1> u r gae lmao e </h1>')"""

"""def signup(request):
	form = UserCreationForm(request.POST)
	return render(request,"app1/signup.html",{'form':form})"""

def signup(request):
	if request.user.is_authenticated:
		return HttpResponse("<h1> you are authenticated </h1>")
	form = UserCreationForm(request.POST)
	if form.is_valid():
		form.save()
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username = username, password = password)
		login(request,user)
	username1 = form.cleaned_data.get('username')
	return render(request,"app1/signup.html",{'form':form})


def logged(request):
	return render(request,"app1/userlogged.html")

def logoutview(request):
	logout(request)
	return HttpResponse("<h2> you were , logged out bro </h2>")

def loginview(request):
	return render(request,"app1/loginview.html")

def process(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username = username,password = password)
	login(request,user)
	return HttpResponseRedirect(reverse('app1:logged'))

def addbook(request):
	return render(request,"app1/addbook.html")

def addbookproc(request):
	bookname = request.POST['title']
#	b1 = Book(title = bookname)
#	b1.save()
	b1 = Book.objects.create(title = bookname)
	prod1 = Producer('quickstart-events', bookSerializer)
#	sendbook1 = Book.objects.get(title = bookname)
#	prod1.send(sendbook1)
	prod1.send(b1)
	return HttpResponseRedirect(reverse('app1:bookadded'))

def bookadded(request):
	return render(request,"app1/bookadded.html")