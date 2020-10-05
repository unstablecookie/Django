from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
	path('', views.index, name='index'),
	path('books/', views.BookListView.as_view(), name='books'),
	path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
	path('authors/', views.AuthorListView.as_view(), name='authors'),
	path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
	path('signup/',views.signup, name = 'signup'),
	path('process/',views.process, name = 'process'),
	path('logged/',views.logged, name = 'logged'),
	path('logout/',views.logoutview, name = 'logout'),
	path('login/',views.loginview, name = 'login'),
	path('addbook/',views.addbook, name = 'addbook'),
	path('addbookproc/',views.addbookproc, name = 'addbookproc'),
	path('bookadded/',views.bookadded, name = 'bookadded'),
]