from django.db import models

# Create your models here.
class Student(models.Model):
    s_id=models.IntegerField(unique=True)
    fname=models.CharField(max_length=80)
    lname=models.CharField(max_length=80)
    div=models.CharField(max_length=10)
    mail = models.EmailField()
    marks=models.FloatField()
