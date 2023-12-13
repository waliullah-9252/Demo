from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    phone_no = models.CharField(max_length=11)

    def __str__(self):
        return self.name