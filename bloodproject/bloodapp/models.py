from django.db import models

# Create your models here.
class Places(models.Model):
    name=models.CharField(max_length=250,unique=True)
    desc=models.TextField(blank=True)
    class Meta:
        db_table='Places'
    def __str__(self):
        return self.name

class Booking(models.Model):
    name=models.CharField(max_length=250,unique=True)
    age=models.IntegerField()
    address=models.TextField(blank=True)
    bgroup=models.CharField(max_length=250)
    mob=models.IntegerField()
    class Meta:
        db_table='Booking'
    def __str__(self):
        return self.name

