from django.test import TestCase, Client
from django.contrib.auth import models


class ClientTestCase(TestCase):
    def setUp(self) -> None:
        '''
        Create a user to use in tests
        '''
        client1 = models.User.objects.create(
            password = 'fabiano123',
            username = 'fabiano',
            first_name = 'Fabiano',
            last_name = 'Venturini',
            email = 'fabiano@fabiano.com',
        )
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
        self.assertEquals(self.p1.is_staff, False)

    def test_login_user_true(self):
        '''
        Test if the user can do login
        '''
        # Todo terminar
        response = self.c.login(email='fabiano@fabiano.com', password='fabiano123')
        self.assertEquals(response.__str__(), 'True')