from django.contrib import admin
from polls.models import Poll
from polls.models import Choice

## Customize Form
class ChoiceInline(admin.TabularInline): #StackedInline
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	"""Customize the admin form"""
	# fields = ['pub_date','question']
	fieldsets = [
		('Questions', 		 {'fields': ['question']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question']

# Register your models here.
admin.site.register(Poll, PollAdmin)
# admin.site.register(Choice)
