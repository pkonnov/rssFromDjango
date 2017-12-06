from django.db import models
import datetime

# Create your models here.


class Post(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=60)
    text = models.TextField()
    date = models.DateField(default=str(datetime.datetime.now()))
    image = models.ImageField(blank=True,
     upload_to='images/blog/%Y/%m/%d',
      help_text='300x250px',
       verbose_name='url img')

    def __str__(self):
        return str(self.id) + "_" + str(self.title)