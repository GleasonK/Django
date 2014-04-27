## Use forms to extend models
from django import forms
## Import our model
from models import Article

## Import new class
class ArticleForm(forms.ModelForm):

	class Meta:
		## Now knows it is bound to that article
		model = Article

		## Tell it not to display the likes field:
		fields = ('title','body', 'pub_date')
