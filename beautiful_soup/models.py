from django.db import models


# Create your models here.
class Link(models.Model):

    address = models.URLField(default='Missing address', null=True, blank=True)
    name = models.CharField(default='Missing name', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
