from django.db import models
from django.urls import reverse
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=30)
    ceo = models.CharField(max_length=20)
    location = models.CharField(max_length=40)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})