from django.db import models

# Create your models here.

class Videos(models.Model):
    video_id= models.CharField(max_length=20)
    title=models.TextField()
    description=models.TextField() 
    thumbnail= models.TextField()
    duration= models.IntegerField()
    publish_date= models.TextField()