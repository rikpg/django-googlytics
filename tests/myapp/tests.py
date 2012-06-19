#
# myapp/tests.py
#
from django.test import TestCase
from django.template import RequestContext, Template
from django.conf import settings
from mock import MagicMock

TEMPLATE = Template('{{ googlytics_code }}')


class TestEmptyKey(TestCase):

    def setUp(self):
        settings.GOOGLE_ANALYTICS_KEY = ''
        self.mock_request = MagicMock(name='request')

    def test_empty_key(self):
        """Tests empty key value."""
        c = RequestContext(self.mock_request)
        self.assertEqual(TEMPLATE.render(c), u'')

    def tearDown(self):
        del settings.GOOGLE_ANALYTICS_KEY


class TestNotEmptyKey(TestCase):

    def setUp(self):
        settings.GOOGLE_ANALYTICS_KEY = 'U-XXX-X'
        self.mock_request = MagicMock(name='request')

    def test_fake_key(self):
        """Tests with a fake kay value."""
        c = RequestContext(self.mock_request)
        self.assertTrue(TEMPLATE.render(c))

    def tearDown(self):
        del settings.GOOGLE_ANALYTICS_KEY


class TestAdminIgnore(TestCase):

    def setUp(self):
        settings.GOOGLE_ANALYTICS_KEY = 'U-XXX-X'
        settings.GOOGLE_ANALYTICS_IGNORE_ADMIN = True
        self.mock_request = MagicMock(name='request')

    def test_not_auth_user(self):
        """Tests not authenticated user."""
        self.mock_request.user.is_authenticated.return_value = False

        c = RequestContext(self.mock_request)
        self.assertTrue(TEMPLATE.render(c))

    def test_auth_not_staff_user(self):
        """Tests authenticated but not staff user."""
        self.mock_request.user.is_authenticated.return_value = True
        self.mock_request.user.is_staff = False

        c = RequestContext(self.mock_request)
        self.assertTrue(TEMPLATE.render(c))

    def test_staff_user(self):
        """Tests authenticated but not staff user."""
        self.mock_request.user.is_authenticated.return_value = True
        self.mock_request.user.is_staff = True

        c = RequestContext(self.mock_request)
        self.assertEqual(TEMPLATE.render(c), u'')

    def tearDown(self):
        del settings.GOOGLE_ANALYTICS_KEY
        del settings.GOOGLE_ANALYTICS_IGNORE_ADMIN
        del self.mock_request
