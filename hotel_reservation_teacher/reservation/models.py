from django.db import models
from user.models import CustomUser
from django.utils import timezone

# Create your models here.

class Room(models.Model) :
    name = models.CharField(max_length=20)
    how_many_accept = models.IntegerField(default=2)
    discription = models.TextField()
    price = models.IntegerField(default=50000)


class Reservation(models.Model) :
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    
    reservation_start_day = models.DateField(default=timezone.now)
    reservation_end_day = models.DateField(default=timezone.now)

    reservation_request_day = models.DateField(default=timezone.now)

    night_num = models.IntegerField(default=1)
    users_num = models.IntegerField(default=2)