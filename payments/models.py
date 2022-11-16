from django.db import models

# Create your models here.

class Status(models.TextChoices):
    SUCCESS = "success", ("Success")
    DUE = "due", ("Due")

class Payment_Status(models.TextChoices):
    SUCCESS = "success", ("Success")
    FAILD = "faild", ("Faild")
    CANCEL = "cancel", ("Cancel")


class Order(models.Model):
    product = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.FloatField()
    total_price = models.FloatField()
    status = models.CharField(max_length=20, choices=Status.choices)
    payment_status = models.CharField(max_length=20, choices=Payment_Status.choices, blank=True, null=True)
    trans_id =  models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.pk)