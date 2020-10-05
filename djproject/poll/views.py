from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from .models import Choice
from .models import Superhero
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from django.utils import timezone
from django.views import generic

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

#def index(request):
#	latest_question_list = Question.objects.order_by('-pub_date')[:5]
#	template = loader.get_template('poll/index.html')
#	contex = {
#		'latest_question_list': latest_question_list,
#		'title':'title,lmao',
#	}
#	return HttpResponse(template.render(contex,request))


def dewei(request):
	str1 = 'we need ebola to nou de wei'
	template = loader.get_template('poll/dewei.html')
	contex = {
		'str1': str1
	}
	return HttpResponse(template.render(contex,request))


#def detail(request, question_id):
#	question = get_object_or_404(Question, pk=question_id)
#	return render(request,'poll/detail.html',{'question': question})


#def results(request, question_id):
#	question = get_object_or_404(Question, pk=question_id)
#	return render(request, 'poll/results.html', {'question': question})




def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'poll/detail.html',{'question': question,'error_message': "select a choice plz"})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('poll:results' , args=(question_id,)))


class IndexView(generic.ListView):
	template_name = 'poll/index.html'
	context_object_name = 'latest_question_list'
	def get_queryset(self):
		"""return the last five published questions. """
#		return Question.objects.all()
		return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'poll/detail.html'
	def get_queryset(self):
		return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'poll/results.html'


"""SUPAHEROES!!!"""


def SuperheroView(request):
	superhero_list = Superhero.objects.all()
	return render(request, "poll/superhero.html",{'superhero_list':superhero_list})

def SuperheroAddView(request):
	return render(request,"poll/superheroadd.html")

def SuperheroProcess(request):
	supname = request.POST['sname']
	suppower = request.POST['spower']
	supdate = request.POST['sdate']
	supnum = request.POST['snum']
	s1 = Superhero(name = supname , date = supdate, superpower= suppower, number = supnum)
	s1.save()
	return HttpResponseRedirect(reverse('poll:sadded'))

def Sadded(request):
	return render(request,"poll/sadded.html")


#login \ sign up

"""def home_view(request):
	return render(request,'home.html')"""

"""def signup_view(request):
	form = UserCreationForm(request.POST)
	if form.is_valid():
		form.save()
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password1')
		user = authenticate(username = username,password = password)
		login(request,user)
	return render(request,"poll/signup.html",{'form': form})"""



def home_view(request):
	return render(request,'poll/home.html')

def signup_view(request):
	form = UserCreationForm(request.POST)
	if form.is_valid():
		form.save()
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password1')
		user = authenticate(username = username,password = password)
		login(request,user)
	return render(request,"poll/signup.html",{'form': form})
















































