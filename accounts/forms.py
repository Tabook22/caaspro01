from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm #this is a djanog built in form we can use it out of the box
from django.contrib.auth.models import User

#here we want to make sure that if we save our ReisterForm it will be saved inside the user model
class RegisterForm(UserCreationForm):
    firstname =forms.CharField(max_length="200")
    lastname=forms.CharField(max_length="200")
    email = forms.EmailField() # notice this email filed will be not shown, because the parent class, don't know any thing about, os i need to add a new property called fileds, which is a dictionary containg the list of fileds i need them to be shown

    class Meta:
	# here we are to change the user model when we save something inside this RegisterForm. 
    # to do that we creating an instance of the user mode and we are going to add new things to it, whe we save the form
        model = User 
        # here we are going to define a new property called fields, which will layout out extactly where my field i want them to be
        # this property is imporatn for th parent class user to show the newlly added fileds such as email (added above) in our case
        # here am tying the fields in the order i want them to be shown inside my form
        fields = ["firstname","lastname","username", "email", "password1", "password2"]
        # notice after creating all this we can use our RegisterForm instide of UserCreationForm