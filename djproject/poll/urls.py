from django.urls import path
from . import views

app_name = 'poll'
#urlpatterns = [
#	path('',views.index, name = 'index'),
#	path('dewei/',views.dewei, name = 'dewei'),
#	path('<int:question_id>/',views.detail, name = 'detail'),
#	path('<int:question_id>/results/',views.results, name = 'results'),
#	path('<int:question_id>/vote/',views.vote, name = 'vote'),
#]

urlpatterns = [
	path('',views.IndexView.as_view(), name = 'index'),
	path('<int:pk>/',views.DetailView.as_view(), name = 'detail'),
	path('<int:pk>/results/' ,views.ResultsView.as_view(), name = 'results'),
	path('<int:question_id>/vote/',views.vote ,name = 'vote'),
	path('superhero/',views.SuperheroView , name = 'superhero'),
	path('superheroadd/',views.SuperheroAddView , name = 'superheroadd'),
	path('superheroprocess/',views.SuperheroProcess, name = 'superheroprocess'),
	path('sadded.html',views.Sadded, name = 'sadded'),
	path('home/',views.home_view, name = 'home'),
	path('signup/',views.signup_view, name = 'signup'),
	]