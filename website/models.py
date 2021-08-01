from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Categorias(models.TextChoices):
    TECH = 'TC', 'Tecnologia'
    CR = 'CR', 'Curiosidades'
    GR = 'GR', 'Geral'

class Post(models.Model):
    
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.CharField(max_length=80)
    created_date = models.DateTimeField(default=timezone.now)
    Categories = models.CharField(
        max_length = 2,
        choices = Categorias.choices,
        default = Categorias.GR,

        )

    def __str__(self):
        return self.title
    
