from django.db import models

# Create your models here.

class Infos(models.Model):
    title = models.CharField(max_length=800)
    price = models.IntegerField()
    content = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    contact = models.CharField(max_length=500)
    joined_date = models.DateField(null=True)


class Users(models.Model):
    price = models.IntegerField()
    duration = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    address = models.CharField(max_length=500)
    contact = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to='images/')
    def __str__(self):
         return f"{self.address} {self.price}"

class Userinfos(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    homeaddress = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)





class UploadImage(models.Model):
    caption = models.CharField(max_length=200)
    image1 = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.caption