from django.db import models

# Create your models here.


class urlShortener(models.Model):
    longurl = models.CharField(max_length=255)
    shorturl = models.CharField(max_length=10)

    def __str__(self):
        return self.shorturl
