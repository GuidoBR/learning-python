# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from casa_app.casa_model import Casa
from routes.casas.home import index, delete
from gaebusiness.business import CommandExecutionException
from gaegraph.model import Node
from mommygae import mommy
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        mommy.save_one(Casa)
        template_response = index()
        self.assert_can_render(template_response)


class DeleteTests(GAETestCase):
    def test_success(self):
        casa = mommy.save_one(Casa)
        redirect_response = delete(casa.key.id())
        self.assertIsInstance(redirect_response, RedirectResponse)
        self.assertIsNone(casa.key.get())

    def test_non_casa_deletion(self):
        non_casa = mommy.save_one(Node)
        self.assertRaises(CommandExecutionException, delete, non_casa.key.id())
        self.assertIsNotNone(non_casa.key.get())

