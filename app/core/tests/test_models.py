from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):
    def test_create_user_with_email_sucessful(self):
        # Test Creating a new user with an email is sucessfull

        email = 'test@gmail.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email ='test@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())