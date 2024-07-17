from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.CharField(max_length=200)
    color = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Application(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    AppointmentDate = models.CharField(max_length=200)
    Department = models.CharField(max_length=200)
    Doctor = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class member(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name
