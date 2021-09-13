from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse,resolve
from .forms import CustUserCreationForm
from .views import SignupPageView


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user('will', 'will@gmail.com', 'testpass123')
        self.assertEqual(user.username,'will')
        self.assertEqual(user.email,'will@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser('superadmin', 'superadmin@gmail.com', 'testpass123')
        self.assertEqual(admin_user.username,'superadmin')
        self.assertEqual(admin_user.email,'superadmin@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

class SignUpPageTests(TestCase):

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_templates(self):
        self.assertEqual(self.response.status_code,200)
        self.assertTemplateUsed(self.response,'users/signup.html')
        self.assertContains(self.response,'Sign Up')
        self.assertNotContains(self.response,'Hi dont show me')

    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form,CustUserCreationForm)
        self.assertContains(self.response,'csrfmiddlewaretoken')

    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.__name__,SignupPageView.as_view().__name__)