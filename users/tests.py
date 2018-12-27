from django.test import TestCase
from django.core import mail

import logging

from .models import CustomUser

log = logging.getLogger(__name__)


class IndexTests(TestCase):

    def setUp(self):
        CustomUser.objects.create_user(email='mail@gmail.com', password='motdepasse', first_name='moi')


    def test_no_user_logged(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_authenticated)

    def test_user_can_login(self):
        is_authenticated = self.client.login(username='mail@gmail.com', password='motdepasse')
        self.assertTrue(is_authenticated)

    def test_auth_user_recognized_on_index(self):
        self.client.login(username='mail@gmail.com', password='motdepasse')
        response = self.client.get('/')
        self.assertTrue(response.context['user'].is_authenticated)

    def test_wrong_password(self):
        is_authenticated = self.client.login(username='mail@gmail.com', password='wrong')
        self.assertFalse(is_authenticated)

    def test_wrong_username(self):
        is_authenticated = self.client.login(username='wrong@gmail.com', password='motdepasse')
        self.assertFalse(is_authenticated)

    # password reset
    def test_reset_password_view_with_mail(self):
        response = self.client.post('/user/reset_password/', {'email': 'mail@gmail.com',})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['form_validated'])

    def test_reset_password_view_no_mail(self):
        response = self.client.post('/user/reset_password/')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['form_validated'])

    def test_valid_users_mail(self):
        self.client.post('/user/reset_password/', {'email': 'mail@gmail.com', })
        self.assertEqual(len(mail.outbox), 1)

    def test_invalid_user_mail(self):
        self.client.post('/user/reset_password/', {'email': 'bad@gmail.com', })
        self.assertEqual(len(mail.outbox), 0)

    def test_reset_password_link(self):
        self.client.post('/user/reset_password/', {'email': 'mail@gmail.com', })
        mail_body = mail.outbox[0].body
        link = mail_body[79:115]
        response = self.client.get(f'/user/{link}/')
        self.assertEqual(response.status_code, 200)

    def test_reset_password(self):
        self.client.logout()
        self.client.post('/user/reset_password/', {'email': 'mail@gmail.com', })
        mail_body = mail.outbox[0].body
        link = mail_body[79:115]
        self.client.post(f'/user/{link}/', {
            'password': 'test',
            'password_check': 'test'
        })
        is_authenticated = self.client.login(username='mail@gmail.com', password='test')
        self.assertTrue(is_authenticated)

    # password change

    def test_change_password_link_logged_used(self):
        response = self.client.get('/user/change_password/')
        self.assertEqual(response.status_code, 200)

    def test_change_password_link_no_user_logged(self):
        self.client.logout()
        response = self.client.get('/user/change_password/')
        self.assertEqual(response.status_code, 200)