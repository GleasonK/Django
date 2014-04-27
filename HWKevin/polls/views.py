

from polls.models import Choice, Poll

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """
        Return the last five published polls.
        Not including the ones in the future
        """
        return Poll.objects.filter(
        	pub_date__lte=timezone.now()
        	).order_by('-pub_date')[:5]
        # return Poll.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'
    def get_queryset(self):
        return Poll.objects.filter(pub_date__lte=timezone.now())
        # return Poll.objects.order_by('-pub_date')[:5]



class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'

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

