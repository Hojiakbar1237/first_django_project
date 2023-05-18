from django.db import models

# Create your models here.
class Followers(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Follower'

    def __str__(self):
         return self.full_name
