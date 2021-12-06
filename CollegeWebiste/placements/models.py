from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    emailid =models.EmailField(max_length=100)
    phoneno = models.IntegerField()
    remarks = models.EmailField(max_length=1000)
    date = models.DateField()

    def __str__(self):
        return self.name



