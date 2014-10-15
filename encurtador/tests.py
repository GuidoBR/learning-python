from django.test import TestCase
from .models import Link
from django.core.urlresolvers import reverse


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

    def test_pagina_inicial(self):
        """
        Testa que a página inicial existe e contém um formulário
        """
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("form", response.context)

    def test_formulario_encurtador(self):
        """
        Verifica se ao submeter o formulário, recebo uma URL
        """
        url = "http://www.google.com/"
        response = self.client.post(reverse("home"),
                                    {"url": url}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn("link", response.context)

        l = response.context["link"]
        self.assertEqual(url, l.url)

    def test_redirecionamento_para_link_original(self):
        """
        Testa o redirecionamento para o Link original
        """
        url = "http://www.google.com/"
        l = Link(url=url)
        short_url = Link.encurtar(l)
        response = self.client.get(
            reverse("redirect_short_url",
                    kwargs={"short_url": short_url}))
        self.assertRedirects(response, url)
