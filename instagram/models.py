from django.db import models

# Create your models here.
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