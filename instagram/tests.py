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
   
    
               
        
 
