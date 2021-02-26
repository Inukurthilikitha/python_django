from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord,Test_Table,Schools,Students # insted we can import all models as below
#from first_app.models import *
from .forms import * # imported for form model 
from django.views.generic import (View,TemplateView,
                                    ListView,DetailView,
                                    CreateView,UpdateView,DeleteView)
from . import models #should be after generic views is loaded
 #importing for View - class based view , TemplateView - template view

# you can create functions to load html pages for data rendering
# we can use model forms , to show form without creating import
# and another function that show form with manual code

class CBVview(View): #class based view
    def get(self,request):
        return HttpResponse("<h2><em>This is calling from class based view</em></h2>")

class CBVTemplateView(TemplateView):
    template_name = "index.html" #need to assign to template_name variable only
    extra_context = {'injectme': 'basic injection','called_from':'CBV'} #for passsing arguments

    #another way to pass arguments
    # def get_context_data(self,**kwargs):# **kwargs also written as *args https://www.geeksforgeeks.org/args-kwargs-python/
    #     extra_context = super().get_context_data(**kwargs)
    #     extra_context['injectme'] = 'basic injection';
    #     extra_context['called_from'] = 'CBV';
    #     return extra_context

class SchoolsListView(ListView):
    #if ntg template_name is specified , it takes view name as context_object_name+"_list" i.e schools_list
    context_object_name = "schools"
    model = models.Schools

class SchoolDetailView(DetailView):
    context_object_name = "school_details" #should be used as variable containing all the data
    model = models.Schools
    template_name = 'first_app/school_detail_view.html'

class SchoolCreateView(CreateView):
    fields = ('school_name','principal_name','location')
    model = models.Schools

class SchoolUpdateView(UpdateView):
    fields = ('school_name','principal_name','location')
    model = models.Schools

class SchoolDeleteView(DeleteView):
    #create html file with model name + "_confirm_delete.html"
    #schools_confirm_delete.html
    model = models.Schools #  we can directly access data by using model name in lowercase
    success_url = reverse_lazy('first_app:school_list')

def index(request): #function based view
	my_dict ={'insert_here':{'first':'This is render through view to html inner dict'}};
	return render(request,'index.html',context=my_dict);

def first_app(request):
	my_dict ={'insert_here':'This is render through view to html inside first_app'};
	return render(request,'first_app/first_app.html',context=my_dict);

def test(request):
	return HttpResponse("<em>Hello Likitha!Welcome</em><br><h2>To see all details type first_app</hr>")

def render_data(request):
	table_data = Test_Table.objects.order_by('name')
	my_dict ={'test_table_data':table_data}
	return render(request,'first_app/render_data.html',my_dict)

def form_data(request):
	form = FormExample()
	if request.method == 'POST':
		form = forms.FormExample(request.POST)
		if form.is_valid():
			print("Entered Details are")
			print(form.cleaned_data['name'])
			print(form.cleaned_data['email'])
			print(form.cleaned_data['textarea'])
	return render(request,'first_app/form_page.html',{'form':form})

def model_form(request):
	form = ModelForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		#return index(request) #returns to home page
		return redirect('/first_app/first_one/') #redirect using url path
		#return redirect('render_data') #redirect using url name
	return render(request,'first_app/form_page.html',{'form':form}) 

def other(request):
    return render(request,'first_app/other.html')

def temp_index(request):
    context={'text':"hello world", 'number':100}
    return render(request,'first_app/index.html', context)

def relative(request):
    return render(request,'first_app/relative_url_templates.html')

def userinfo(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoMode(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoMode()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'first_app/register.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})