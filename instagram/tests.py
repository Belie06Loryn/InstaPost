from django.test import TestCase
from .models import Foto,Comment,Follower,Profile
class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.profile= Profile(image = 'Jam.jpeg', name ='Muriuki', email ='james@moringaschool.com',bio = 'hdeydfedf')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(self.profile,Follower)

    def tearDown(self):
        Follower.objects.all().delete()
   
    def test_save(self):
        self.profile.save_profile()
        profile= Profile.objects.all()
        self.assertTrue(len(profile)>=1) 

    def test_upd(self):
        profile = Profile.objects.filter(id=1)
        profile.update(image = 'Kam.jpeg', name ='Murki', email ='james@morischool.com',bio = 'hdefedf')
        search = Profile.objects.filter(id=1)
        self.assertNotEqual(search,'Kam.jpeg')

    def test_dele(self):
        self.profile.save_profile()
        profi = Profile.objects.all()
        self.assertTrue(len(profi)>=0)              
        
 
class CommentTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.comment= Comment(comment = 'Fun')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(self.comment,Comment)    

     # Testing Save Method
    def test_save(self):
        self.comment.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) >= 1)  

    def test_upd(self):
        comment = Comment.objects.filter(id=1)
        comment.update(comment ='Art')
        search = Comment.objects.filter(id=1)
        self.assertNotEqual(search,'Art') 

    