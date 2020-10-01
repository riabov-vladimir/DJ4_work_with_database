from django.db import models


class Phone(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.TextField()
    price = models.PositiveIntegerField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()
