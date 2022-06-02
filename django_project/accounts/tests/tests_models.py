from django.test import TestCase, Client
from django.contrib.auth import models
from django.contrib.auth import authenticate
from django.urls import reverse

class ClientTestCase(TestCase):
    def setUp(self) -> None:
        '''
        Create a user to use in tests
        '''
        self.client1 = models.User.objects.create(
            username='fabiano',
            first_name='Fabiano',
            last_name='Venturini',
            email='fabiano@fabiano.com',
            is_active=True,
        )
        # Tip: https://stackoverflow.com/questions/2619102/djangos-self-client-login-does-not-work-in-unit-tests
        self.client1.set_password('fabiano123')
        self.client1.save()
        # various tests needs this variable
        self.p1 = models.User.objects.get(username='fabiano')
        self.c = Client()

    def test_return_username_str(self):
        '''
        Test the username return
        '''
        self.assertEquals(self.p1.__str__(), 'fabiano')

    def test_return_email(self):
        '''
        Test the email return
        '''
        self.assertEquals(self.p1.email, 'fabiano@fabiano.com')

    def test_return_full_name(self):
        '''
        Test the return of full name
        '''
        self.assertEquals(self.p1.get_full_name(), 'Fabiano Venturini')

    def test_is_staff(self):
        '''
        Test if the user is member of the team
        '''
        self.assertFalse(self.p1.is_staff)

    def test_login_user_true_with_email(self):
        '''
        Test if the user can login with email
        '''
        user = authenticate(username='fabiano@fabiano.com', password='fabiano123')
        self.assertTrue(user.is_authenticated)

    def test_login_with_password_wrong(self):
        '''
        Test if the user can do login with wrong password
        '''
        user = authenticate(username='fabiano@fabiano.com', password='wrongPassword')
        self.assertIsNone(user)
