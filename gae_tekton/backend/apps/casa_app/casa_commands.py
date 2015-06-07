# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode, NodeSearch, DeleteNode
from casa_app.casa_model import Casa



class CasaSaveForm(ModelForm):
    """
    Form used to save and update Casa
    """
    _model_class = Casa
    _include = [Casa.foto,
                Casa.preco,
                Casa.descricao,
                Casa.titulo,
                Casa.tamanho,
                Casa.endereco]


class CasaForm(ModelForm):
    """
    Form used to expose Casa's properties for list or json
    """
    _model_class = Casa


class GetCasaCommand(NodeSearch):
    _model_class = Casa


class DeleteCasaCommand(DeleteNode):
    _model_class = Casa


class SaveCasaCommand(SaveCommand):
    _model_form_class = CasaSaveForm


class UpdateCasaCommand(UpdateNode):
    _model_form_class = CasaSaveForm


class ListCasaCommand(ModelSearchCommand):
    def __init__(self):
        super(ListCasaCommand, self).__init__(Casa.query_by_creation())

