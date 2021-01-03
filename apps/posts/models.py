from django.db import models
from django.contrib.auth.models import User # get first model for connect



class Tag(models.Model):
	title = models.CharField('Title', max_length = 50)
	description = models.TextField('TEXT', null=True, blank=True)
	parent = models.TextField('parent', null=True, blank=True)
	child = models.TextField('child', null=True, blank=True)
	synonym = models.TextField('synonym', null=True, blank=True)
	

	
	
	
	

class Post(models.Model):
	class TypeChoise(models.IntegerChoices):
		publish = 0
		hide = 1
		trush = 2
		beta = 3
		alfa = 4
	class LangChoise(models.IntegerChoices):
		publish = 0
		hide = 1
		trush = 2
		beta = 3
		alfa = 4
	title = models.CharField('Title', max_length = 50)
	description = models.TextField('TEXT', null=True, blank=True)
	date = models.DateTimeField('date publish')
	image = models.ImageField(upload_to='images/', null=True, blank=True)
	second_images = models.ImageField(upload_to='images/', null=True, blank=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	type = models.IntegerField('type', choices=TypeChoise.choices, null=True, blank=True)
	lang = models.IntegerField('lang', choices=LangChoise.choices, null=True, blank=True)
	black_horse = models.IntegerField('black_horse', default=0)
	virus = models.IntegerField('virus', default=0)
	file_torrent = models.FileField(upload_to='torrent/', null=True, blank=True)
'''
for field
views
downloads
number of bookmarked
critics rating
user rating
money
finished watching
'''
class EachTag(models.Model):
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
	percent = models.IntegerField('black_horse', default=50)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	



class Statistic(models.Model):
	value = models.IntegerField('Value', default=0)
	name = models.CharField('name', max_length = 50)
	post =  models.ForeignKey(Post, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	
	
class Same(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	
class ArrayLinks(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	link = models.TextField('link')
'''
for field
number of comments
'''
class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	author =  models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField('Title', max_length = 50)
	text = models.TextField('TEXT', null=True, blank=True)
	date = models.DateTimeField('date publish')
'''
for field
user rating
'''
class StatisticComment(models.Model):
	value = models.IntegerField('Value', default=0)
	name = models.CharField('name', max_length = 50)
	comment =  models.ForeignKey(Comment, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)


# model for add Extra file from other posts
class ExtraPost(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	author =  models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField('Title', max_length = 50)
	id_file = models.IntegerField('id_file')
	
	
	
	
	

