# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from datetime import datetime, date
from decimal import Decimal
from casa_app.casa_model import Casa
from routes.casas.new import index, save
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        template_response = index()
        self.assert_can_render(template_response)


class SaveTests(GAETestCase):
    def test_success(self):
        self.assertIsNone(Casa.query().get())
        redirect_response = save(foto='foto_string', preco='1.2', descricao='descricao_string')
        self.assertIsInstance(redirect_response, RedirectResponse)
        saved_casa = Casa.query().get()
        self.assertIsNotNone(saved_casa)
        self.assertEquals('foto_string', saved_casa.foto)
        self.assertEquals(1.2, saved_casa.preco)
        self.assertEquals('descricao_string', saved_casa.descricao)

    def test_error(self):
        template_response = save()
        errors = template_response.context['errors']
        self.assertSetEqual(set(['foto', 'preco', 'descricao']), set(errors.keys()))
        self.assert_can_render(template_response)
