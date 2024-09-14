from django.db import models

# Create your models here.
class student(models.Model):
    #id=models.AutoField()
    name= models.CharField(max_length=150)
    Age=models.IntegerField(default=25)
    Address=models.TextField()
    #file=models.FileField()