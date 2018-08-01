from django.contrib.auth.models import User
from django.core import mail
from django.test import TestCase
from hc.api.models import Check

class class LogoutTestCase(TestCase):
    def test_log_out(self):
            self.client.logout()
            r = self.client.post(url)
            self.assertRedirects(r, "/index/")