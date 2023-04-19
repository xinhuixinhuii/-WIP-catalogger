from django.db import models

# Create your models here.

class Photo(models.Model):
    photo = models.ImageField()
    class Meta:
        abstract = True
    
class CatList(Photo):
    name = models.CharField(max_length = 16)
    
    def __str__(self) -> str:
        return self.name