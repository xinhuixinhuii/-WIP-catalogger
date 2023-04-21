from django.db import models

# Create your models here.

class Photo(models.Model):
    photo = models.ImageField()
    class Meta:
        abstract = True
    
class CatList(Photo):
    catListName = models.CharField(max_length = 16, unique = True, default = "Unknown")
