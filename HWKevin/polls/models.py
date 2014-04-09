from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Poll(models.Model):
	question = models.CharField(max_length=200);
	pub_date = models.DateTimeField('date published');

	def __unicode__(self):
		return self.question

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	was_published_recently.admin_order_field = 'pub_date' #Filter
	was_published_recently.boolean = True ## Makes check / handles booleans
	was_published_recently.short_description = 'Published Recently?' #desc

class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice_text = models.CharField(max_length=200)
	vote = models.IntegerField(default=0)

	def __unicode__(self):
		return self.choice_text
