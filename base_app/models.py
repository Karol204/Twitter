from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Tweet(models.Model):
    content = models.CharField(max_length=250)
    creation_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.content} - {self.author}'