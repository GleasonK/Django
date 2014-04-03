from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template # Long way
from django.views.generic.base import TemplateView # Class Template

from article.models import Article

# Create your views here.

def index(request):
	context = { 'articles':Article.objects.all() }
	return render(request, 'article/articles.html', context)

def articles(request):
	context = { 'articles':Article.objects.all() }
	return render(request, 'article/articles.html', context) 

def article(request, article_id=1):
	context = { 'article':Article.objects.get(id=article_id) }
	return render(request, 'article/article.html', context)




def hello(request):
	name = "Kevin"
	html = '<h1> Hello %s </h1>' % name
	return HttpResponse(html)

def helloWithTemp(request):
	name = "Kevin"
	context = {'name':name}
	return render(request, 'article/Hello.html', context)
	# temp = get_template('article/Hello.html')
	# html = temp.render(Context({'name':name}))
	# return HttpResponse(html)

class HelloTemplate(TemplateView):
	template_name = 'article/Hello.html'

	def get_context_data(self, **kwargs):
	    context = super(HelloTemplate, self).get_context_data(**kwargs)
	    context['name'] = "Kevin"
	    return context