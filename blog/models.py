from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author=models.CharField(max_length=25)
    subject=models.CharField(max_length=40)
    content=models.TextField()
    pdate=models.CharField(max_length=30)
    ptime=models.CharField(max_length=30)
    class Meta:
        ordering=['-pk']
class Comment(models.Model):
    pid=models.CharField(max_length=25)
    postedby=models.CharField(max_length=25)
    comment=models.TextField()
    cdate=models.CharField(max_length=20)
    ctime=models.CharField(max_length=30)
    class Meta:
        ordering=['-pk']
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='profile_pics/img_avatar.png',upload_to='profile_pics')
    def __str__(self):
        return f'{self.user.username}Profile'