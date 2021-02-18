from django.db import models
from django.contrib.auth.models import User #to use users from admin

# SuperUserInformation
# User: likki
# Email: likki@test.com
# Password: testhere

# Here we can add tables we want to create 
# and run migration scripts 
# we need to add it in admin.py to visible the table in admin interface

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class Test_Table(models.Model):
    name = models.CharField(max_length=264,unique=True)
    added_date = models.DateField()
    added_by   = models.CharField(max_length=264)
    def __str__(self):
        return "Name is {} - Added by {}".format(self.name, self.added_by) #used to customize the view in admin panel

class UserProfileInfo(models.Model):
    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete=models.CASCADE) #we have already users table under admin
    portfolio_site = models.URLField(blank=True)
    # pip install pillow to use this!
    profile_pic = models.ImageField(upload_to='first_app/profile_pics',blank=True) #blank=true used to make image as optional

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username