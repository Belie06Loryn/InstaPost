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

                 
        
 
