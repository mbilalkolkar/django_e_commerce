from django.db import models

# Create your models here.


class Countries(models.Model):
    country_name = models.CharField(unique=True, max_length=255)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"
