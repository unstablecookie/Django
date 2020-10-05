from django.db import models
from django.utils import timezone
import datetime



# Create your models here.

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	dewei = models.BooleanField(default=True)
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now

	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text

class Superhero(models.Model):
	name = models.CharField(max_length=100)
	date = models.DateField(auto_now=False,auto_now_add=False)
	superpower = models.CharField(max_length=100)
	number = models.IntegerField(default=0)
	def __str__(self):
		return self.name