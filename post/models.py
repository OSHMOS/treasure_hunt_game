from django.db import models

# Create your models here.


class Post(models.Model):
    author = models.CharField(max_length=10)
    present = models.TextField()

    def __str__(self):
        return self.author
