from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.
def view(request):
    return render(request, "main/view.html", {})

# inside views.py
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    if ls in response.user.todolist.all():
        if response.method == "POST":
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()

            elif response.POST.get("newItem"):
                txt = response.POST.get("new")

                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                     print("invalid")
        return render(response, "main/list.html", {"ls":ls})
    return render(response, "main/home.html", {})

def home(request):
    return render(request, "main/index.html")

def create(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)
        # When a user enter submits the data via form Django first validate and clean the data. 
        # In the process of validation Django creates an attribute called cleaned_data, a dictionary which contains cleaned data only from the fields which have passed the validation tests. 
        if form.is_valid(): #checks if all form fields contains a valid data, if so then those valid data will be placed inside the cleaned_data object, for there we can access those data
            n = form.cleaned_data["name"] # from the vaild fields which were placed inside the cleaned_data attribute we need only the "name"
            t = ToDoList(name=n)
            t.save()
            print(f"--------{n}")
            request.user.todolist.add(t)  # adds the to do list to the current logged in user
        return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewList()

    return render(request, "main/create.html", {"form":form})