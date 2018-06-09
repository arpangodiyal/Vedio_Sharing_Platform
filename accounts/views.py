from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.mail import send_mail
from .forms import register_form,login_form,verify_form,Vedios_form,Comments_form
from .models import Vedios,Comments
import random
#from .models import Vedios
#from .forms import Vedios_form,register_form,login_form,verify_form

# Create your views here.
code="0"
username=""
password=""
first_name=""
last_name=""
email=""
def home(request):
	context={"username":username}
	print(context)
	return render(request,"home.html",context)

def upload(request):
	if request.method=="POST":
		form=Vedios_form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect("/home")
		else:
			print("Form is not valid")
	if request.method=="GET":
		form=Vedios_form()
		context={"form":form}
		return render(request,"upload.html",context)
def watch(request):
	a=Vedios.objects.all()
	context={"data":a}
	return render(request,"watch.html",context)
def play(request,id=None):
	if request.method=="POST":
		instance=get_object_or_404(Vedios,id=id)
		form=Comments_form(request.POST)
		if form.is_valid():
			p=Comments(vediono=instance,comment=form.cleaned_data.get('comment'),user=username)
			p.save()
			return redirect("/accounts/"+str(id))
	else:
		a=get_object_or_404(Vedios,id=id)
		c=Comments.objects.filter(vediono=id)
		form=Comments_form()
		context={"data":a,"data2":c,"form":form,"username":username}
		return render(request,"play.html",context)

def register_view(request):
	if request.method=="POST":
		form=register_form(request.POST)
		if form.is_valid():
			global username
			username=form.cleaned_data.get('username')
			print(username)
			global password
			password=form.cleaned_data.get('password')
			global email
			email=form.cleaned_data.get('email')
			global first_name
			first_name=form.cleaned_data.get('first_name')
			global last_name
			last_name=form.cleaned_data.get('last_name')
			c=User.objects.filter(username=username).count()
			if c==1:
				messages.error(request,"Username in use")
				return redirect("/accounts/register")
			no=Email(email)
			print(c)
			if no==0:
				messages.error(request,'Enter the correct E-mail address')
				return redirect("/accounts/register")
			else:
				#user=User.objects.create_user
				#create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name,step=1)
				#user.save()
				return redirect("/accounts/verify")
	else:
		form=register_form()
		context={"form":form}
		return render(request,"register.html",context)
def login_view(request):
	if request.method=="POST":
		form=login_form(request.POST)
		if form.is_valid():
			global username
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password')
			user=authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				return redirect("accounts/home")
			else:
				 messages.error(request,'Enter correct username or password')
				 return redirect("/")
	else:
		form=login_form()
		context={"form":form}
		return render(request,"login.html",context)

def logout_view(request):
	logout(request)
	return redirect("/")
def verify_view(request):
	print(code)
	if request.method=="POST":
		form=verify_form(request.POST)
		if form.is_valid():
			key=form.cleaned_data.get('key')
			if key==code:
				user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
				user.save()
				return redirect("/")
			else:
				messages.error(request,"Enter the correct key")
				return redirect("/accounts/verify")

	else:
		form=verify_form()
		context={"form":form}
		return render(request,"verify.html",context)
def Email(to):
	code1=random.randint(100,999)
	code2=random.randint(250,750)
	global code
	code=str(code1)+str(code2)
	m=send_mail('Verify', 
				code, 
				'arpangodiyal24@gmail.com',
				[to], 
				fail_silently=True)
	
	return m










