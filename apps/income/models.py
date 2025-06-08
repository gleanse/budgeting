from django.db import models
from django.contrib.auth.models import User


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    date= models.DateField(auto_now_add=True)
    note = models.TextField(max_length=250)

    def __str__(self):
         return f"{self.user} got income on {self.category} - PHP {self.amount} at {self.date}"
