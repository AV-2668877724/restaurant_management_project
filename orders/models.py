from django.db import models

class OrderStatus(models.Model):
    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name

class Coupon(models.Model):
    code=models.CharField(max_length=50, unique=True)
    discount_percentage=models.DecimalField(max_digits=5,decimal_place=2)
    is_active=models.BooleanField(default=True)
    valid_from=models.DateField()
    valid_until=models.DateField()

    def __str__(self):
        return self.code

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
