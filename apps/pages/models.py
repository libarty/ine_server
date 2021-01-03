from django.db import models
from django.contrib.auth.models import User # get first model for connect

# Create model for docs 
class Page(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField('title', max_length = 50)
	text = models.TextField('text',null=True, blank=True)
	def __str__(self):
		return self.title