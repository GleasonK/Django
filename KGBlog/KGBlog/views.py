from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
#from django.contrib.auth.forms import UserCreationForm
from forms import MyRegistrationForm

def login(request):
	## c = context
	c = {}
	c.update(csrf(request)) ## going to pass in csrf object
	return render(request, 'login.html', c)

def auth_view(request):
	username = request.POST.get("username", "")
	password = request.POST.get("password", "")

	##returns user object if found, if none, returns None
	user = auth.authenticate(username=username, password=password)
	

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
	## Look into request.user docs
	c = { 'full_name':request.user.username }
	return render(request, 'loggedin.html', c)

def invalid_login(request):
	return render(request, 'invalid.html')

def logout(request):
	auth.logout(request)
	return render(request, 'logout.html')

def register_user(request):
	if request.method == 'POST':
		## Form should take in everything from the POST array
		#form = UserCreationForm(request.POST)
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/register_success')

	args = {}
	args.update(csrf(request))

	## Empty at start, knows how to render its fields, but not data
	#args['form'] = UserCreationForm();
	args['form'] = MyRegistrationForm();
	print args

	return render(request, 'register.html', args)

def register_success(request):
	return render (request, 'register_success.html')

