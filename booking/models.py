from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Baloon(models.Model):
    name = models.CharField(max_length=30)
    image = models.CharField(max_length=30)


class Place(models.Model):
    number = models.IntegerField()
    baloon = models.ForeignKey(Baloon, on_delete=models.CASCADE)


class Booking(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.DO_NOTHING)
