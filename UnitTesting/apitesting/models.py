from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=50)
    author_name = models.CharField(max_length=50, null=True)
    publish_date = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self) -> str:
        return self.name