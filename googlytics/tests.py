from django.test import TestCase
from django.test.client import RequestFactory
from django.template import RequestContext
from django.contrib.auth.models import User, AnonymousUser


class TestAnonUsers(TestCase):
    """Tests various settings for anonymous users."""

    def setUp(self):
        factory = RequestFactory()
        self.request = factory.get('foo.html')
        self.request.user = AnonymousUser()

    def test_empty_key(self):
        with self.settings(GOOGLE_ANALYTICS_KEY=''):
            context = RequestContext(self.request)
        self.assertEqual(context['googlytics_code'], u'')

    def test_ignore_admin_not_set(self):
        context = RequestContext(self.request)
        self.assertTrue(context['googlytics_code'])

    def test_ignore_admin_set_false(self):
        with self.settings(GOOGLE_ANALYTICS_IGNORE_ADMIN=False):
            context = RequestContext(self.request)
        self.assertTrue(context['googlytics_code'])

    def test_ignore_admin_set_true(self):
        with self.settings(GOOGLE_ANALYTICS_IGNORE_ADMIN=True):
            context = RequestContext(self.request)
        self.assertTrue(context['googlytics_code'])


class TestLoggedUsers(TestAnonUsers):
    """Tests various settings for logged (but not staff/admin) users."""

    def setUp(self):
        factory = RequestFactory()
        self.request = factory.get('foo.html')
        self.user = User.objects.create_user(username='Bob', password='secret')
        self.user.is_staff = False
        self.request.user = self.user


class TestStaffLoggedUsers(TestLoggedUsers):
    """Tests various settings results for logged staff/admin users."""

    def setUp(self):
        super(TestStaffLoggedUsers, self).setUp()
        self.user.is_staff = True

    def test_ignore_admin_set_true(self):
        with self.settings(GOOGLE_ANALYTICS_IGNORE_ADMIN=True):
            context = RequestContext(self.request)
        self.assertEqual(context['googlytics_code'], u'')
