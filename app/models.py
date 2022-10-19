from django.db import models

# Create your models here.
class Booking(models.Model):
    Booking = models.CharField(max_length=150)

    def __str__(self):
        return self.Booking


class Person(models.Model):
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    Phno = models.CharField(max_length=10)
    Email = models.CharField(max_length=30)
    Number_of_people = models.IntegerField()
    Booking = models.ForeignKey('Booking', on_delete = models.SET_NULL,null=True)
    Date_of_Movie = models.DateField(null=True,blank=True)
    


    def __str__(self):
        return f"{self.First_name} {self.Last_name} Booked {self.Booking}"
