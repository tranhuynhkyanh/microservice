from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def add_likes(self):
        self.likes += 1
        self.save()
