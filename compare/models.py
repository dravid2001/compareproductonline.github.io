from django.db import models

# Create your models here.

class Contact(models.Model):
    id = models.AutoField(primary_key=True, default=0)
    name = models.CharField(max_length=60, default="")
    email = models.CharField(max_length=60, default="")
    phone = models.CharField(max_length=60, default="")
    address = models.CharField(max_length=60, default="")
    city = models.CharField(max_length=60, default="")
    state = models.CharField(max_length=60, default="")
    zip = models.CharField(max_length=60, default="")
    query = models.CharField(max_length=60, default="")


    def __str__(self):
        return self.name