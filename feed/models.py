from django.db import models

# Create your models here.

class Post(models.Model):
    text = models.TextField(max_length=240)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.text[0:100]