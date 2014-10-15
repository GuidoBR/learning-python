from django.test import TestCase
from .models import Link

class ShortenerText(TestCase):
    def test_encurtar(self):
        """
        Testa que a URL é encurtada
        """
        url = "http://www.google.com/"
        l = Link(url=url)
        url_encurtada = Link.encurtar(l)
        self.assertLess(len(url_encurtada), len(url))

    def test_recuperar_link(self):
        """
        Testa que a URL encurtada e a URL original são a mesma
        """
        url_original = "http://www.google.com/"
        l = Link(url=url_original)
        url_encurtada = Link.encurtar(l)
        l.save()
        url_expandida = Link.expandir(url_encurtada)
        self.assertEqual(url_original, url_expandida)


