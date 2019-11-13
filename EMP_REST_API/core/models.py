from django.db import models

# Create your models here.
class Employee(models.Model):
    id=models.IntegerField(blank=True,null=False,primary_key=True)
    employee_name=models.TextField(max_length=30,null=False,blank=False, default='Enter your name')
    employee_salary=models.IntegerField(blank=True,null=False,default=100000000) 
    employee_age=models.IntegerField(blank=False)
    profile_image=models.URLField(default='Enter the path of the pic',blank=True)

    def __str__(self):
        return self.employee_name


