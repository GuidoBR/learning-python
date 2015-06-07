# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from datetime import datetime, date
from decimal import Decimal
from base import GAETestCase
from casa_app.casa_model import Casa
from routes.casas import rest
from gaegraph.model import Node
from mock import Mock
from mommygae import mommy


class IndexTests(GAETestCase):
    def test_success(self):
        mommy.save_one(Casa)
        mommy.save_one(Casa)
        json_response = rest.index()
        context = json_response.context
        self.assertEqual(2, len(context))
        casa_dct = context[0]
        casa_expected = [
            'id',
            'creation',
            'foto',
            'preco',
            'descricao',
            'titulo',
            'tamanho',
            'endereco'
        ]
        self.assertSetEqual(set(casa_expected), set(casa_dct.iterkeys()))
        self.assert_can_serialize_as_json(json_response)


class NewTests(GAETestCase):
    def test_success(self):
        self.assertIsNone(Casa.query().get())
        json_response = rest.new(None, foto='foto_string', preco='1.2', descricao='descricao_string')
        db_casa = Casa.query().get()
        self.assertIsNotNone(db_casa)
        self.assertEquals('foto_string', db_casa.foto)
        self.assertEquals(1.2, db_casa.preco)
        self.assertEquals('descricao_string', db_casa.descricao)
        self.assert_can_serialize_as_json(json_response)

    def test_error(self):
        resp = Mock()
        json_response = rest.new(resp)
        errors = json_response.context
        self.assertEqual(500, resp.status_code)
        self.assertSetEqual(set(['foto', 'preco', 'descricao']), set(errors.keys()))
        self.assert_can_serialize_as_json(json_response)


class EditTests(GAETestCase):
    def test_success(self):
        casa = mommy.save_one(Casa)
        old_properties = casa.to_dict()
        json_response = rest.edit(None, casa.key.id(), foto='foto_string', preco='1.2', descricao='descricao_string')
        db_casa = casa.key.get()
        self.assertEquals('foto_string', db_casa.foto)
        self.assertEquals(1.2, db_casa.preco)
        self.assertEquals('descricao_string', db_casa.descricao)
        self.assertNotEqual(old_properties, db_casa.to_dict())
        self.assert_can_serialize_as_json(json_response)

    def test_error(self):
        casa = mommy.save_one(Casa)
        old_properties = casa.to_dict()
        resp = Mock()
        json_response = rest.edit(resp, casa.key.id())
        errors = json_response.context
        self.assertEqual(500, resp.status_code)
        self.assertSetEqual(set(['foto', 'preco', 'descricao']), set(errors.keys()))
        self.assertEqual(old_properties, casa.key.get().to_dict())
        self.assert_can_serialize_as_json(json_response)


class DeleteTests(GAETestCase):
    def test_success(self):
        casa = mommy.save_one(Casa)
        rest.delete(None, casa.key.id())
        self.assertIsNone(casa.key.get())

    def test_non_casa_deletion(self):
        non_casa = mommy.save_one(Node)
        response = Mock()
        json_response = rest.delete(response, non_casa.key.id())
        self.assertIsNotNone(non_casa.key.get())
        self.assertEqual(500, response.status_code)
        self.assert_can_serialize_as_json(json_response)

