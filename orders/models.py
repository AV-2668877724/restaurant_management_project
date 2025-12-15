from django.db import models

class OrderStatus(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Order(models.Model):
    # existing fields (example)
    order_number = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    # ✅ NEW FIELD (THIS IS THE TASK)
    status = models.ForeignKey(
        OrderStatus,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.order_number
