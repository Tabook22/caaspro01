from django.db import models
from django.contrib.auth.models import User #we import the user model

# Create your models here.
#to dolist will be different for each different user this is the idea
class ToDoList(models.Model):
    # the idea here is make every dolist we create will linked to different user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True) # <--- added #that means every user we create will be linked to a user account
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist=models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text=models.CharField(max_length=300)
    complete=models.BooleanField()

    def __str__(self):
        return self.text
