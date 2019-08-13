from django.db import models


class Pairs(models.Model):
    roman = models.CharField(max_length=5)
    arabic = models.IntegerField()

    def __str__(self):
        return self.roman

