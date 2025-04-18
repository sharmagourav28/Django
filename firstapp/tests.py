from django.db import models

#must to be derived from models
class Employee(models.Model):  # has to be derived from "Model"
    name = models.CharField(max_length=250) # charfield is class 
    department = models.CharField(max_length=250)

    def __str__(self):
        return self.name+"    "+self.department

