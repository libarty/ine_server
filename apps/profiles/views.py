from django.shortcuts import render, redirect # for create html
# redirect page
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
# foe filter
from django.db.models import Q


from django.contrib import auth # for authorization
# import models 
from django.contrib.auth.models import User # get first model for update
from . models import *
from posts.models import *
# Create your views here.

from django.contrib.auth.hashers import check_password
from django.contrib.auth.password_validation import validate_password
# get current time
import datetime
from django.utils import timezone


import re




# for send Message to email
from django.core.mail import send_mail

import random

# page
def get_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip
# page
def enter_user(request,username,password):
	user = auth.authenticate(username=username, password=password)
	if user is not None:
		auth.login(request, user)
		return True
	else:
		return False


# Login User Page
def return_sesion(name,req):
	val = req.POST.get(name, '')
	if val == 'N0n3':
		del req.session[name]
	elif not val == '':
		req.session[name] = val
	try:
		return req.session[name]
	except KeyError:
		pass

# check field validate text

def ValidateName(text):
	if re.search(r'[^a-z0-9_]', text):
		return '004.1'
	elif len(text) > 20 or len(text) < 3:
		return '004.2'
	try:
		User.objects.get(username=text)
		return '004.3'
	except:
		return False
def ValidatePassword(text,text2=False):
	text2 = text2 or text
	if not text == text2:
		return '005.1'
	try:
		validate_password(text)
		return False
	except:
		return '005.2'
		
		
		
def ValidateEmail(text):
	if not '@' in text or  not '.' in text:
		return '006.1'
	try:
		User.objects.get(email=text)
		return '006.2'
	except:
		return False

def ValidatePhone(text):
	if not len(text) == 9:
		return '007.1'
	try:
		ExtraUser.objects.get(phone=text)
		return '007.2'
	except:
		return False










number_list = {
	'lang_ar':'0',
	'lang_ca':'0',
	'lang_cz':'0',
	'lang_de':'0',
	'lang_en':'0',
	'lang_es':'0',
	'lang_eu':'0',
	'lang_fr':'0',
	'lang_gr':'0',
	'lang_he':'0',
	'lang_hi':'0',
	'lang_it':'0',
	'lang_ja':'0',
	'lang_ml':'0',
	'lang_pl':'0',
	'lang_ru':'0',
	'lang_sv':'0',
	'lang_zh':'0',
}





from django import template
                    

from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes



def login(request):
	# set args
	args = {}
	args['where'] = 1
	args['login_error'] = None
	home = '/pages/search/'
	args['login'] = return_sesion('Login',request)
	args['password'] = return_sesion('Password',request)
	# check user
	if request.user.is_authenticated or request.POST.get('Redirect', ''):
		url = reverse('profiles:profile_page', args=(str(request.user.id)))
		return redirect(url)  # redirecting the user to the page home
	else:
		# User Enter
		if request.POST.get('Entry', ''):
			# Check if a username exists or email
			username = args['login']
			# check if in field email
			if '@' in username:
				try:
					username = User.objects.get(email=username)
				except:
					args['login_error'] = '001.2'
			else:
				try:
					username = User.objects.get(username=username)
				except:
					args['login_error'] = '001.1'
			# check password
			if args['login_error'] is None:
				password = args['password']
				result = enter_user(
					request,
					username,
					password
				)
				if result:
					url = reverse('profiles:profile_page', args=(str(username.id)))
					return redirect(url)  # redirecting the user to the page home
				else:
					args['login_error'] = '002'
		# Registration Menu
		elif request.POST.get('Registration', '') or request.POST.get('Cancel',''):
			args['where'] = 2
			# Delete old data
			try:
				del request.session['code_1']
				del request.session['code_2']
				#del request.session['set_user']
			except KeyError:
				pass

		# Back to login page
		elif request.POST.get('Back', ''):
			args['where'] = 1

		# Save session for check user
		elif request.POST.get('Next', ''):
			try:
				AlreadyIp.objects.get(ip_name=get_ip(request))
				args['login_error'] = '003'
			except:
				args['password_agin'] = return_sesion('PasswordA',request)
				args['email'] = return_sesion('Email',request)
				args['phone'] = return_sesion('Phone',request)
				log = args['login']
				pas = args['password']
				pasa = args['password_agin']
				ema = args['email']
				pho = args['phone']
				return_sesion('select_contry_number',request)
				
				
				
				
				
				
				if not args['login_error']:
					args['login_error'] = ValidateName(log)
				if not args['login_error']:
					args['login_error'] = ValidatePassword(pas,pasa)
				if not args['login_error']:
					args['login_error'] = ValidateEmail(ema)
				if not args['login_error']:
					args['login_error'] = ValidatePhone(pho)
			if args['login_error']:
				args['where'] = 2
			else:
				# Save random code
				for x in range(2):
					random_num = ''
					for y in range(6):
						random_num = random_num + str(random.randint(0, 9))

					request.session['code_'+str(x+1)] = random_num
				# send a letter
				send_mail(
					'Code',
					'Code-1 for email:' + request.session['code_1'] + ' , Code-2 for phone:' + request.session['code_2'],
					'from@example.com',
					[request.POST.get('Email', '')],
					fail_silently=False,
				)
				args['where'] = 3

		# User Registration
		elif request.POST.get('Check', ''):
			if	request.POST.get('code1', '') == request.session['code_1'] and \
				request.POST.get('code2', '') == request.session['code_2']:
				
				users = User(
					username=request.session['Login'],
					email=request.session['Email'],
				)
				
				ph = number_list[request.session['select_contry_number']]+request.session['Phone']
				users.set_password(request.session['Password'])
				extra = ExtraUser(
					user=users,
					phone=ph,
				)
				already = AlreadyIp(ip_name=get_ip(request))
				users.save()
				extra.save()
				already.save()
				# enter
				username = request.session['Login']
				password = request.session['Password']
				result = enter_user(request, username, password)
				if result:
					url = reverse('profiles:profile_page', args=(str(request.user.id)))
					return redirect(url)  # redirecting the user to the page home
				else:
					args['login_error'] = '002'
					return render(request, 'login.html', {'args': args})  # connect html template
			else:
				args['login_error'] = '008'
				args['where'] = 3
		elif request.POST.get('Restore', ''):
			args['where'] = 4
		elif request.POST.get('Res', ''):
			args['where'] = 4
			
			
			
			#htmltemp = template.loader.get_template('login/send_letter.html')
			

			
			
			#print(htmltemp.render(c))
			
			
			
			val =  request.POST.get('Restore_val','')
			# check if in field email
			if '@' in val:
				try:
					user = User.objects.get(email=val)
				except:
					args['login_error'] = '001.2'
			else:
				try:
					user = User.objects.get(username=val)
				except:
					args['login_error'] = '001.1'
					
			if not args['login_error']:
				
				
				
				
				
				user_token = default_token_generator.make_token(user)
				print(user_token)
				user_uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
				user_uidb64 = ''.join(user_uidb64)
				print(user_uidb64)
				url = reverse('profiles:change_password', args=(user_uidb64,user_token))
				print(url)
				# send a letter
				send_mail(
					'Restore password',
					'your login:'+user.username+' your password:'+user.password,
					'from@example.com',
					[user.email],
					fail_silently=False,
				)
					
					
					
		
		return render(request, 'login.html', {'args': args})  # connect html template
		
		
		
# Function for show User Profile Page  
 
#request.GET.get("tab", "") # get value from http//?tab=1 &==and
# {{ request.get_full_path }} # return full url curent page
# {{ args.get }}





#test form
from . form import *



#paginations
from django.core.paginator import Paginator


def length_paginations(val):
	return {
	'l_l': val,
	'l_f': 0 - val,
	'l_n': val - 1,
	'l_p': 0 - val + 1
	}

def profile_page(request, user_id):
	#print(request.get_full_path)
	args = {}
	
	# test form
	args['form'] = ExForm()
	
	

	

	
	
	# Check if user exists
	try :
		args['user'] = User.objects.get(id = user_id)
		args['user_allow'] = True if  request.user.id == user_id and request.user.is_authenticated else False
		args['get'] = request.GET.get("tab", "")
		try :
			args['extra'] = args['user'].extrauser;
		except:
			pass
		try :
			args['though'] = ThoughtUser.objects.filter(Q(user_id=user_id) | Q(com_thought__user_id=user_id)).order_by('-pud_date').distinct()
			paginator = Paginator(args['though'], 1) # Show 25 contacts
			page = request.GET.get('page')
			args['contacts'] = paginator.get_page(page)
			
			args['length'] = length_paginations(2)
			
			
			
		except:
			pass
		
		
		  # redirecting the user to the page home
		
		#args['though'] = ThoughtUser.objects.filter(Q(connect_id=user_id) | Q(comment_article__user_id=user_id))
		# paginator = Paginator(args['though'], 1) # Show 25 contacts
		# page = request.GET.get('page')
		# contacts = paginator.get_page(page)
		# args['contacts'] = paginator.get_page(page)
		'''
		args['though'] = args['user'].thoughtuser_set.order_by('-id')[:10]
		
		from django.urls import reverse

url = reverse('article:add', kwargs={'id': id})
		'''
		
		#{% url 'profiles:add_think' args.user.id %}
		
		
		
		
	except:
		return redirect(reverse('pages:none'))
	try :
		args['extra_user'] = ExtraUser.objects.get(user = user_id)
	except:
		pass
	
		
		
	return render(request, 'profile.html', {'args':args })
		

		
def replace_shortcode(text,res,type='html',val=False,obj=False,url=False,first=''):
	block = re.findall(res, text)
	if block:
		for line in block:
			# get words without tags
			cline = re.findall(r'cast">(.+?)\</', line)
			# check array
			if not cline:
				words = re.findall(r'\w+', line)
			else:
				words = re.findall(r'\w+', cline[0])
			new_line = ''
			for word in words:
				if (type=='html') :
					for tag in val:
						if (tag==val[-1]):
							new_line = new_line + tag
						else:
							new_line = new_line + tag + word
				if (type=='object') :
					# get object from models
					try:
						number = int(word)
						my_obj = obj.objects.get(id = word)
					except ValueError:
						try:
							my_obj = obj.objects.get(**{val: word})
						except :
							pass
					try:
						# get url from models
						get_url = reverse(url, args=(str(my_obj.id)))
						# create html
						link_tag = '<a href="'+get_url+'">'+first+word+'</a>'
						new_line = new_line + link_tag
					except :
						new_line = new_line + 'ERROR404'
				# replace the old words to new words
			text = text.replace(line, new_line)
	return text
		
def fast_shortcode(text,typ='user'):
	type = 'object'
	val = 'title'
	if (typ=='user'):
		val = 'username'
		obj = User
		url = 'profiles:profile_page'
		first= '@'
		text = replace_shortcode(text,r'@\w+',type,val,obj,url,first)
		text = replace_shortcode(text,r'\<div class="user_block_cast">.+?\</div>',type,val,obj,url,first)
	elif (typ=='tag'):
		obj = Tag
		url = 'profiles:profile_page'
		first= '#'
		text = replace_shortcode(text,r'#\w+',type,val,obj,url,first)
		text = replace_shortcode(text,r'\<div class="tag_block_cast">.+?\</div>',type,val,obj,url,first)
	elif (typ=='post'):
		obj = Post
		url = 'profiles:profile_page'
		first= '№'
		text = replace_shortcode(text,r'№\w+',type,val,obj,url,first)
		text = replace_shortcode(text,r'\<div class="post_block_cast">.+?\</div>',type,val,obj,url,first)
	return text
		
		
# Add a think in page
def add_think(request, user_id):
	try :
		user_get = User.objects.get(id = user_id)
		# delete old text
		thought = user_get.thoughtuser_set.order_by('pud_date')
		print(thought)
		if thought.count() > 100:
			thought.first().delete()
	except:
		return redirect(reverse('pages:none'))
	# get text
	content = request.POST.get('post_thought', '')
	print('-------------------')
	#print(content)
	print('-------------------')
	# text filters
	content = fast_shortcode(content,'user')
	content = fast_shortcode(content,'tag')
	content = fast_shortcode(content,'post')
	user_get.thoughtuser_set.create(text=content,pud_date=timezone.now())
	print('-------------------')
	# come back
	return HttpResponseRedirect(reverse('profiles:profile_page', args = (str(user_id)))+'?tab=thought');


# Add a think in page
def add_com_think(request,page_id, think_id):
	try :
		thing = ThoughtUser.objects.get(id = think_id)
		thingcom = thing.commentthinkuser_set.order_by('pud_date')
		if thingcom.count() > 100:
			thingcom.first().delete()
	except:
		return redirect(reverse('pages:none'))
	# get text
	content = request.POST.get('post_thought', '')
	# text filters
	content = fast_shortcode(content,'user')
	content = fast_shortcode(content,'tag')
	content = fast_shortcode(content,'post')
		
		
	thing.commentthinkuser_set.create(text=content,pud_date=timezone.now(),user=request.user)

	# come back
	return HttpResponseRedirect(reverse('profiles:profile_page', args = (str(page_id)))+'?tab=thought');





'''

	try :
		user = User.objects.get(id = user_id)
	except:
		return redirect(reverse('pages:none'))
		
		
	# create a think
	content = request.POST.get('post_thought', '')
	content = replace_shortcode(content,res,html)
	
	
	
	
	
	
	replace_shortcode(content,r'\[.+?\]',['<a class="redirect_url" href="','">#','</a>'])
	return HttpResponseRedirect(reverse('profiles:profile_page', args = (user.id,)));
	
	'''
	
def delete_think(request, think_id):
	try :
		think = ThoughtUser.objects.get(id = think_id)
		think.delete()
	except:
		raise Http404('404 not found')
	# come back
	return HttpResponseRedirect(reverse('profiles:profile_page', args = (str(request.user.id))));

def delete_com_think(request, think_com_id):
	try :
		com = CommentThinkUser.objects.get(id = think_com_id)
		com.delete()
	except:
		raise Http404('404 not found')
	# come back
	return HttpResponseRedirect(reverse('profiles:profile_page', args = (str(request.user.id))));

				
				
def change_user(request, user_id):
	args = {}
	try :
		user = User.objects.get(id = user_id)
		ex = user.extrauser
	except:
		return redirect(reverse('pages:none'))
		
		
		
	# check if the password is correct
	check_pass = request.POST.get('user_pass_check_field', '')
	if user.check_password(check_pass) :
		# get values
		# for users model
		# user name
		username = request.POST.get('user_name_field', '')
		error = ValidateName(user.username)
		if not error:
			user.username = username
		# email
		email = request.POST.get('user_email_field', '')
		error = ValidateEmail(email)
		if not error:
			user.email = email
		#phone
		phone = request.POST.get('user_phone_field', '')
		error = ValidatePhone(phone)
		if error:
			ex.phone = phone
		# color
		color1 = request.POST.get('icon_img_text', '')
		color2 = request.POST.get('icon_img_back', '')
		ex.icon_colors = color1+','+color2
		# images
		ex.icon_id = request.POST.get('icon_img', '')
		ex.back_id =request.POST.get('back_img', '')
		# password
		password = request.POST.get('user_pass_field', '')
		error = ValidatePassword(password)
		if not error:
			user.set_password(password)
		ex.save()
		user.save()
		
	
	
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('profiles:profile_page', args = (str(user_id)))+'?tab=info');
	else :
		return HttpResponseRedirect(reverse('profiles:login'));
	
	
	
				


				
				
				
				
				
				
		