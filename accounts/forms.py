from .models import Vedios,login_model,register_model,verify_model,Comments
from django import forms

class Vedios_form(forms.ModelForm):
	class Meta:
		model=Vedios
		fields=["vedio","name"]
class Comments_form(forms.ModelForm):
	class Meta:
		model=Comments
		fields=['comment']
class login_form(forms.ModelForm):
	class Meta:
		model=login_model
		fields='__all__'
		widgets={'password':forms.PasswordInput()}

class register_form(forms.ModelForm):
	class Meta:
		model=register_model
		fields='__all__'
		widgets={'password':forms.PasswordInput()}
class verify_form(forms.ModelForm):
	class Meta:
		model=verify_model
		fields="__all__"
		widgets={'key':forms.PasswordInput()}
