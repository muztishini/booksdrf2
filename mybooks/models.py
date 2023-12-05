from django.db import models


class Books(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    year = models.PositiveSmallIntegerField()
    isbn = models.PositiveBigIntegerField()
