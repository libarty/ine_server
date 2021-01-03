from django.db import models
from django.contrib.auth.models import User  # get first model for update


# user Progress for fun
class Progress(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField('progress_name', max_length=50)
	description = models.CharField('progress_description', max_length=360)


# model of add extra field for model User
class ExtraUser(models.Model):
	# model for chose id icon
	class IconChoose(models.IntegerChoices):
		icon2 = 2
		icon3 = 3
		icon4 = 4
		icon5 = 5
		icon6 = 6
		icon7 = 7
		icon8 = 8
		icon9 = 9
		icon10 = 10
		icon11 = 11
	class BackgroundChoose(models.IntegerChoices):
		back1 = 1
		back2 = 2
		back3 = 3
		

	# field for connect to model User
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	
	# field for send the verification code 2
	phone = models.CharField('Phone',max_length=15,)
	
	
	
	
	

	# field settings

	# field for chose svg icon
	icon_id = models.IntegerField('Icon ID', choices=IconChoose.choices, default=8)
	
	back_id = models.IntegerField('Background ID', choices=BackgroundChoose.choices, default=1)
	
	# save color field for svg icon
	icon_colors = models.CharField('Color', max_length=50, default='#d4d4d8,#22222e')
	#icon_color_2 = models.CharField('Color 2', max_length=14, null=True, blank=True)
	#icon_color_3 = models.CharField('Color 3', max_length=14, null=True, blank=True)
	# save karma user for user with role Critic
	karma = models.IntegerField('Karma', default=0)
	# measures the author's skill
	level = models.IntegerField('Level', default=1)
	# user balance for author posts
	money = models.IntegerField('Money', default=0)
	# chose setting filer array
	filter = models.TextField('filter', null=True, blank=True)
	
	
	# user progress for fun
	progress = models.ManyToManyField(Progress, blank=True)

	def __str__(self):
		return self.user.username


# Archive User for save posts in your own directory
class ArchiveUser(models.Model):
	# model for chose type folder
	# if chose folder name show in directory
	# if chose post name show post thumbnail can only be if user add post in favorite
	class ArchiveChoose(models.IntegerChoices):
		folder = 0
		post = 1

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField('archive_title', max_length=50)
	type = models.IntegerField('archive_type', choices=ArchiveChoose.choices)
	parent = models.IntegerField('parent folder id')
	child = models.TextField('child folder id', null=True, blank=True)

	def __str__(self):
		return self.name


# Think User for save mini post in page user no more 100
class ThoughtUser(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.CharField('think_text', max_length=360)
	pud_date = models.DateTimeField('think_pud_date')
	change_date = models.DateTimeField('think_change_date', null=True, blank=True)
	def __str__(self):
		return self.text

# Comment to Think from users no more 100
class CommentThinkUser(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	think = models.ForeignKey(ThoughtUser, on_delete=models.CASCADE, related_query_name ='com_thought')
	text = models.CharField('comment_think_text', max_length=360)
	pud_date = models.DateTimeField('comment_think_pud_date')
	def __str__(self):
		return self.text



# list Favorite User every month user have to pay the donate amount
# if user don't have enough money all field delete 
class FavoriteUser(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	id_user = models.IntegerField('id_user')
	donate = models.IntegerField('donate_user')

	def __str__(self):
		return self.id_user


# list Favorite Post for if User want watch post later
class FavoritePost(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	id_post = models.IntegerField('id_post')

	def __str__(self):
		return self.id_post


# list ip are already in the system
# function against duplicate users
class AlreadyIp(models.Model):
	ip_name = models.CharField('ip_name', max_length=50)

	def __str__(self):
		return self.ip_name
