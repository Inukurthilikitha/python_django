from django.conf.urls import url
from first_app import views

app_name = 'first_app'
urlpatterns = [
	url(r'^$', views.index,name="index"),
	url(r'^first_one/', views.index,name="index"),
	url(r'^form_data/', views.form_data,name="form_data"),
	url(r'^model_form/', views.model_form,name="model_form"),
	url(r'^render_data/', views.render_data,name="render_data"),
	url(r'^first_app/', views.first_app,name="first_app"),
	url(r'^other/',views.other,name='other'),
	url(r'^relative/',views.relative,name='relative'),
	url(r'^temp_index/',views.temp_index,name='temp_index'),
	url(r'^userinfo/',views.userinfo,name='userinfo'),
]