from django.db import models
from django.conf import settings


class MenuCategory(models.Model):
    name = modes.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name=models.CharField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(
        MenuCategory,
        on_delete=models.CASCADE,
        related_name='menu_items'
    )

    is_featured= models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name= models.CharField(max_length=255)
    address= models.TextField()

    has_delivery = models.BooleanField(default= False)

    def __str__(self):
        return self.name

class Note(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notes'
    )
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.owner})"
