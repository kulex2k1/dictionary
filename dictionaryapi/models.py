from django.db import models

# Create your models here.
class Dict_word(models.Model):
    word = models.CharField( max_length=250)

    def __str__(self):
        return self.word
     

