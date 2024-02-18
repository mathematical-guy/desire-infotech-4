from django.db import models
from django.contrib.auth.models import User


">"
class Order(models.Model):  
    name = models.CharField(max_length=200)
    address = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    person = models.ForeignKey(
        to="order_management.Person", on_delete=models.CASCADE, related_name="person_orders")

    def __str__(self) -> str:
        return f"{self.name}-{self.date}"


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()



class AadharDetail(models.Model):
    aadhar_no = models.CharField(max_length=12)
    aadhar_expiry = models.DateField()
    person = models.OneToOneField(to=Person, on_delete=models.PROTECT)