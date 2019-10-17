from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    image = models.ImageField(upload_to = 'profiles/',null=True)
    bio = models.CharField(max_length =6000)

    def save_profile(self):
        self.save()

    def dele_profile(self):
        self.delete() 

    @classmethod
    def update_profile(cls,id):
        profile = cls.objects.filter(id=id).update(id=id)
        return profile     

    def __str__(self):
        return self.bio            

class Comment(models.Model):
    comment = models.CharField(max_length =6000)

    def save_comment(self):
        self.save()

    def dele_comment(self):
        self.delete() 

    @classmethod
    def update_comment(cls,id):
        comment = cls.objects.filter(id=id).update(id=id)
        return comment     

    def __str__(self):
        return self.comment   

class Foto(models.Model):
    image = models.ImageField(upload_to = 'photos/',null=True)
    name = models.CharField(max_length =40)
    caption = models.TextField(max_length =6000)
    like = models.TextField(max_length =6000)
    profile = models.ForeignKey(Profile)
    comments = models.ForeignKey(Comment ,null=True)
     
    def save_pic(self):
        self.save()

    def dele_pic(self):
        self.delete() 

    @classmethod
    def image_by_id(cls,id):
        found = cls.objects.filter(id = id)
        return found

    @classmethod
    def update_pic(cls,id):
        imaje = cls.objects.filter(id=id).update(id=id)
        return imaje          

class Follower(models.Model):
    user = models.ForeignKey(User)
    profile = models.ForeignKey(Profile)

    def save_follower(self):
        self.save()               