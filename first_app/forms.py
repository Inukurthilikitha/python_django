from django import forms
from django.core import validators 
from .models import * 

#here we can configure the forms we need and add validations if needed
#here we have model form to create form based on the structure we provided in model

#https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/

def check_for_text(value):
	if value[0]!= 'L':
		raise forms.ValidationError('Name starts with L')

class FormExample(forms.Form):
	name = forms.CharField(required=False,validators=[check_for_text]) #input field with validations and is not req
	email = forms.EmailField() #input with email
	verify_email = forms.EmailField(label='verify_email')
	textarea = forms.CharField(widget=forms.Textarea,validators=[
			validators.MinLengthValidator(5),
			validators.MaxLengthValidator(10,'Please enter text with 10 chars')]) #textarea
	hiddenfield = forms.CharField(required=False,widget=forms.HiddenInput) #hidden field
	
	# def clean_hiddenfield(self):
	# 	hiddendata = self.cleaned_data['hiddenfield']
	# 	if len(hiddendata) > 0 :
	# 		raise forms.ValidationError('Hidden Field contains value')
	# 	return hiddendata

	def clean(self):
		all_clean_data = super().clean() #it cleans entire form data
		email = all_clean_data['email']
		verify_email = all_clean_data['verify_email']
		if email!=verify_email:
			raise forms.ValidationError('Please enter same emails')

class ModelForm(forms.ModelForm): 
    class Meta: 
        model = Webpage 
        fields = "__all__"	 #includes all the fields in the specified model
        #fields = ['name']	 #shows only fields included here
        #exclude = ('url',)  #if we add here then the field is not going to display in ui form

    name = forms.CharField(validators=[check_for_text]) #to add validations

    #here you can clean as above to check data as well

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoMode(forms.ModelForm): 
    class Meta: 
        model = UserProfileInfo 
        exclude = ('user',)
