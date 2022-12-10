from django.test import TestCase
from django.utils import timezone
from users.models import CustomUser, Profile

class CategoryTestCase(TestCase):
    def setUp(self):
        CustomUser.objects.create(
            username='testUser', email='test@email.com', 
            first_name='test', last_name='user', 
            password=''
        )

    def test_model(self):
        cat = CustomUser.objects.get(id=1)
        self.assertEqual(cat.first_name, 'test')

class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username='testUser', email='test@email.com', first_name='test', last_name='user', password='')
        self.user.set_password('secret')
        self.user.save()       
        Profile.objects.create(
            user=self.user,
            first_name='Jim',
            last_name='Halpert', address=123,city='Alabany',
            postal_code=4999, date_of_birth=timezone.now(), photo=None
        )

    def test_contact_model(self):
        item = Profile.objects.get(id=1)
        self.assertEqual(item.first_name, 'Jim')