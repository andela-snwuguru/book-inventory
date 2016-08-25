from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, related_name="books")

    def __str__(self):
        return self.name
