from django.db import models
from catlist.models import CatList


# Create your models here.
class Photo(models.Model):
    photo = models.ImageField()
    
    class Meta: 
        abstract = True

class CatLog(CatList, Photo):
    catLogName = models.ForeignKey(CatList, to_field = 'catListName', on_delete = models.CASCADE, parent_link = True, related_name = 'catlog_ptr', default = "Unknown")
    location = models.JSONField(max_length = 128)
    dateTime = models.DateTimeField()
     