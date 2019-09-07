from django.shortcuts import render
from .models import ToDoList

# Create your views here.
def index(request, id):
    ls=ToDoList.Objects.get(id=id)

    if request.method=="POST":
        if request.POST.get("save"):
            for item in ls.item_set.all():
                if request.POST.get("c" + str(itme.id)=="clicked"):
                    item.complete=True
                else:
                    item.complete=False
                item.save()
        elif request.POST.get("newItem"):
            txt=request.POST.get("new")

            if len(txt)>2:
                ls.item_set.create(text=txt,complete=False)
            else:
                print("invalid")
    return render(request, "main/list.html", {"ls":ls})

def home(request):
    return render(request, "main/index.html")

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

        return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewList()

    return render(response, "main/create.html", {"form":form})