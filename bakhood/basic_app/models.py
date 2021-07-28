from django.db import models
from django.urls import reverse
# Create your models here.

class Bakhood(models.Model):
    name = models.CharField(max_length=256)
    real_name = models.CharField(max_length=256)
    fav_p = models.CharField(max_length=256)
    bak_pic = models.ImageField(upload_to='bak_pics',blank=True, default='bak_pics/user.jpg')
    
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("app:bakdetail",kwargs={'pk':self.pk})

class Sons(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    father = models.ForeignKey(Bakhood,related_name='sons',on_delete=models.CASCADE)
    son_pic = models.ImageField(upload_to='son_pics',blank=True, default='son_pics/user.jpg')
    
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("app:sondetail",kwargs={'pk':self.pk})

# class Photo(models.Model):
#     profile_pic = models.ImageField(upload_to='profile_pics')
    