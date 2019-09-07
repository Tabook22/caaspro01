from django.shortcuts import render,redirect
from .forms import RegisterForm
# Create your views here.
def register(request):
    if  request.method=="POST": #check to see if the form method is POST, which means we are sending data
        form=RegisterForm(request.POST) #create a new instance of that form with all the data it carries
        if form.is_valid(): # if there is no errors in the form 
            form.save() # save the form 
        return redirect("/")
    else: # else if there is an error create a new empty instance of that form
        form=RegisterForm() #create a new instance of the form
    return render(request, "accounts/register.html", {"form":form})