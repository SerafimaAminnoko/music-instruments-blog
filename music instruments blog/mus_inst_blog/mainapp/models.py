from django.db import models

# Create your models here.


class Musinst(models.Model):
    title1 = models.CharField(max_length=100)
    text1 = models.TextField()
    time_create1 = models.DateTimeField(auto_now_add=True)
    time_update1 = models.DateTimeField(auto_now=True)
    is_published1 = models.BooleanField(default=True)

    def __str__(self):
        return self.title1


class Mainpage(models.Model):
    title2 = models.CharField(max_length=100)
    text2 = models.TextField()
    time_create2 = models.DateTimeField(auto_now_add=True)
    time_update2 = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title2

