from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=30)
    contact = models.IntegerField()
    email = models.EmailField(max_length=50)
    age = models.IntegerField()


