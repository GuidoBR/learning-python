from django.test import TestCase
from .models import Link

class ShortenerText(TestCase):
    def test_shortens(self):
        """
        Testa que a URL é encurtada
        """
        url = "http://www.google.com/"
        l = Link(url=url)
        short_url = Link.shorten(l)
        self.assertLess(len(short_url), len(url))
