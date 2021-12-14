from django.db import models
from django.db.models.fields import CharField, DateField, EmailField, IntegerField, TextField
from datetime import datetime  

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=25)
    number = models.CharField(max_length=12)
    email = models.CharField(max_length=30)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Room_type(models.Model):
    room_type_name =models.CharField(max_length=15)
    cost = models.FloatField()

    def __str__(self):
        return self.room_type_name

class Userprofile(models.Model):
    Name= models.CharField(max_length=20)
    status= models.IntegerField(default=1)
    no= models.IntegerField()
    email = models.EmailField()
    address= models.TextField()

    def __str__(self):
        return self.Name



class Room(models.Model):
    room_no=models.IntegerField()
    type = models.ForeignKey(Room_type, on_delete= models.CASCADE)
    room_status =models.BooleanField()

    def __str__(self):
        return str(self.room_no)

class BooKings(models.Model):
    user = models.ForeignKey(Userprofile, on_delete= models.CASCADE)
    checkin_date = models.DateField(default=datetime.now(), blank=True)
    chekout_date= models.DateField()
    room_type = models.ForeignKey(Room, on_delete= models.CASCADE) 

    def __str__(self):
        return str(self.checkin_date)





