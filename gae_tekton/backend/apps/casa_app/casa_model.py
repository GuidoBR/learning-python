# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property


class Casa(Node):
    titulo = ndb.StringProperty(required=False)
    descricao = ndb.StringProperty(required=True)
    foto = ndb.StringProperty(required=True)
    preco = ndb.FloatProperty(required=True)
    endereco = ndb.StringProperty(required=False)
    tamanho = ndb.FloatProperty(required=False)
