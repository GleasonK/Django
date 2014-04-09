from django.contrib import admin
from article.models import Article

## Admin Class

class ArticleAdmin(admin.ModelAdmin):
	fieldsets = [
		('Article',         {'fields':('title','body')}),
		('Date and Likes',  {'fields':('pub_date', 'likes')}),
	]


# Register your models here.
admin.site.register(Article, ArticleAdmin)