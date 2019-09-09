from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.
def view(request):
    return render(request, "main/view.html", {})

# inside views.py
def index(request, id):
    ls = ToDoList.objects.get(id=id) # means get the the list of the names in the ToDoList with an id which is eql to id
    if ls in request.user.todolist.all(): #here we are checking if the list is linked to the current user or not
        if request.method == "POST":
            if request.POST.get("save"):
                for item in ls.item_set.all():
                    if request.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()

            elif request.POST.get("newItem"):
                txt = request.POST.get("new")

                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                     print("invalid")
        return render(request, "main/list.html", {"ls":ls})
    return render(request, "main/home.html", {})

def home(request):
    return render(request, "main/index.html")

def create(request):
    if request.method == "POST":
        form = CreateNewList(request.POST) # adding the data into form
        # When a user enter submits the data via form Django first validate and clean the data. 
        # In the process of validation Django creates an attribute called cleaned_data, a dictionary which contains cleaned data only from the fields which have passed the validation tests. 
        if form.is_valid(): #checks if all form fields contains a valid data, if so then those valid data will be placed inside the cleaned_data object, for there we can access those data
            n = form.cleaned_data["name"] # from the vaild fields which were placed inside the cleaned_data attribute we need only the "name"
            t = ToDoList(name=n)
            t.save()
            request.user.todolist.add(t)  # adds the to do list to the current logged in user
        return HttpResponseRedirect("/%i" %t.id) # here "/%i" means a place for integer, and that integer will be provided from %t.id, because any url with integer will be given to index page please see the urls.py

    else:
        form = CreateNewList() # new empty form to enter data into it

    return render(request, "main/create.html", {"form":form})