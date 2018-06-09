from django.db import models

# Create your models here.

class Vedios(models.Model):
	vedio=models.FileField(upload_to='vedio')
	name=models.CharField(max_length=30)
	updated=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name
class Comments(models.Model):
	vediono=models.ForeignKey(Vedios)
	user=models.CharField(max_length=30,null=True)
	comment=models.TextField(null=True)
	def __str__(self):
		return self.comment
class login_model(models.Model):
	username=models.CharField(max_length=30)
	password=models.CharField(max_length=100)

	def __str__(self):
		return self.username

class register_model(models.Model):
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=30)
	username=models.CharField(max_length=30,unique=True)
	password=models.CharField(max_length=100)
	email=models.CharField(max_length=100)

	def __str__(self):
		return self.username
class verify_model(models.Model):
	key=models.CharField(max_length=100)
	def __str__(self):
		return self.key

