## forms framework
from django import forms
## Authrntication models, bring in the User to fill in user info there
from django.contrib.auth.models import User
## Inherit from the user creation form
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
	## Tell what parts of information you want to pull from format
	## Define a field
	email = forms.EmailField(required=True)
	fName = forms.CharField(label = "First Name", required=True)
	lName = forms.CharField(label = "Last Name" ,required=True)

	class Meta:
		model = User
		fields = ('username', 'fName', 'lName', 'email', 'password1', 'password2')

	##Overwrite the UCF save function
	def save(self, commit=True):
		## False since we dont want to save right away, need to edit
		## If inherited elsewhere must spcify whether we want auto save
		user = super(UserCreationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['fName']
		user.last_name = self.cleaned_data['lName']

		if commit:
			user.save()

		return user