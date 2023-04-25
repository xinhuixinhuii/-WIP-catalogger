from django.db import models
from catlist.models import CatList
from django_cleanup import cleanup

# Create your models here.
class Photo(models.Model):
    photo = models.ImageField()
    
    class Meta: 
        abstract = True

class CatLog(CatList, Photo):
    catLogName = models.ForeignKey(CatList, to_field= 'catListName', on_delete= models.CASCADE, parent_link= True, related_name= 'catlog_ptr', default = "Unknown")
    location = models.JSONField(max_length= 128)
    createdAt = models.DateTimeField(auto_now_add= True, blank=True)
    
    
    @cleanup("createdAt", clean_empty= False)
    def cleanUpLogs(self):
        pass