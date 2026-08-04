from django.test import TestCase
from django.urls import reverse


class PortfolioViewTests(TestCase):
    def test_portfolio_page_loads(self):
        response = self.client.get(reverse('portfolio'))
        self.assertEqual(response.status_code, 200)
