from django.test import TestCase
from django.contrib.auth.models import User
from mock import Mock
import recurly

class TestAccountCreation(TestCase):

    def test_save(self):
        act = recurly.Account
        act.__init__ = Mock(return_value=None)
        act.save = Mock(return_value=None)

        u = User(username="user")
        u.save()

        self.assertEqual(act.save.call_count, 1, "Recurly account not saved")
