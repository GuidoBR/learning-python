# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from datetime import datetime, date
from decimal import Decimal
from casa_app.casa_model import Casa
from routes.casas.edit import index, save
from mommygae import mommy
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        casa = mommy.save_one(Casa)
        template_response = index(casa.key.id())
        self.assert_can_render(template_response)


class EditTests(GAETestCase):
    def test_success(self):
        casa = mommy.save_one(Casa)
        old_properties = casa.to_dict()
        redirect_response = save(casa.key.id(), foto='foto_string', preco='1.2', descricao='descricao_string')
        self.assertIsInstance(redirect_response, RedirectResponse)
        edited_casa = casa.key.get()
        self.assertEquals('foto_string', edited_casa.foto)
        self.assertEquals(1.2, edited_casa.preco)
        self.assertEquals('descricao_string', edited_casa.descricao)
        self.assertNotEqual(old_properties, edited_casa.to_dict())

    def test_error(self):
        casa = mommy.save_one(Casa)
        old_properties = casa.to_dict()
        template_response = save(casa.key.id())
        errors = template_response.context['errors']
        self.assertSetEqual(set(['foto', 'preco', 'descricao']), set(errors.keys()))
        self.assertEqual(old_properties, casa.key.get().to_dict())
        self.assert_can_render(template_response)
