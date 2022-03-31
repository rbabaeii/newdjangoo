from django.db import models
from django.contrib.auth.models import User



class Categories(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.name

# Create your models here.
class Data(models.Model):
    description = models.CharField(max_length= 100)
    dueDate = models.DateField()
    category = models.ForeignKey(Categories , on_delete= models.SET_NULL , null= True)
    user = models.ForeignKey(User , on_delete=models.CASCADE , null= True)
    def __str__(self) -> str:
        return self.description
    # user = models.ForeignKey(User , on_delete=models.CASCADE , null= True)
