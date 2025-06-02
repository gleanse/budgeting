from django.db import models

# Create your models here.
class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    note = models.TextField(max_length=250)

    def __str__(self):
        return f"{self.category} - PHP {self.amount}"

class Income(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    note = models.TextField(max_length=250)

    def __str__(self):
        return f"{self.category} - PHP {self.amount}"