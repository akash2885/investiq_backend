from django.db import models


class Politician(models.Model):
    firstName = models.CharField(max_length=10)
    lastName = models.CharField(max_length=20)
    transaction = models.CharField(max_length=10)
    stock = models.CharField(max_length=10)
    filed = models.DateField()
    traded = models.DateField()

    def __str__(self):
        return self.firstName + ' ' + self.lastName


