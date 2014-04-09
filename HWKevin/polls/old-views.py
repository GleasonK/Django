from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
# from django.shortcuts import Http404
# from django.template import RequestContext, loader
import time

from polls.models import Poll
# Create your views here.

## With render you only need to import render, 
## does all the request work for you

def index(request):
	latest_poll_list = Poll.objects.order_by('-pub_date')[:5].reverse()
	## template = loader.get_template('polls/index.html')
	timenow = time.gmtime()
	times = "Mon " + str(timenow[1]) + " Day " + str(timenow[2])
	context = {'latest_poll_list': latest_poll_list,'time':times}
	return render(request, 'polls/index.html', context)
	# context = RequestContext(request, {
	# 	'latest_poll_list': latest_poll_list,
	# 	'time':times,
	# })
	## output = ', '.join([p.question for p in latest_poll_list])
	# return HttpResponse(template.render(context))

def detail(request, poll_id):
	poll = get_object_or_404(Poll, pk=poll_id)
	return render(request, 'polls/detail.html', {'poll' : poll})
	# try:
	# 	poll = Poll.objects.get(pk=poll_id)
	# except Poll.DoesNotExist:
	# 	raise Http404
	# return render(request, 'polls/detail.html', {'poll' : poll})
	#return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
	poll = get_object_or_404(Poll, pk=poll_id)
	return render(request, 'polls/results.html', { 'poll':poll })

def vote(request, poll_id):
	#return HttpResponse("You're voting on poll %s." % poll_id)
	p = get_object_or_404(Poll, pk=poll_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render (request, 'polls/detail.html', {
			'poll': p,
			'error_message': "You didn't select a choice", 
		})
	else:
		selected_choice.vote += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

