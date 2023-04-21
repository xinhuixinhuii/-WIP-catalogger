from django.db import models
from catlist.models import CatList


# Create your models here.
class Photo(models.Model):
    photo = models.ImageField()
    
    class Meta: 
        abstract = True

class CatLog(CatList):
    #catName = models.ForeignKey(CatList, max_length=16, on_delete = models.CASCADE)
    location = models.JSONField(max_length = 128)
    dateTime = models.DateTimeField()
     
    def new_post(self):
        return self.new_post()