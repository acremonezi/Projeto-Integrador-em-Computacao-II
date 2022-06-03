from django.test import TestCase, Client
from django.urls import reverse


class AccountsViewTestCase(TestCase):
    def test_status_code_200(self):
        response = self.client.get(reverse('account_login'))
        self.assertEquals(response.status_code, 200)

    def test_template_login(self):
        response = self.client.get(reverse('account_login'))
        self.assertTemplateUsed(response, 'account/login.html')

    def test_template_index(self):
        response = self.client.get(reverse('project_index'))
        self.assertTemplateUsed(response, 'accounts/index.html')

    def test_template_base(self):
        response = self.client.get(reverse('project_index'))
        self.assertTemplateUsed(response, 'account/base.html')
