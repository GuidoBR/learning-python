# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from casa_app.casa_commands import ListCasaCommand, SaveCasaCommand, UpdateCasaCommand, CasaForm,\
    GetCasaCommand, DeleteCasaCommand


def save_casa_cmd(**casa_properties):
    """
    Command to save Casa entity
    :param casa_properties: a dict of properties to save on model
    :return: a Command that save Casa, validating and localizing properties received as strings
    """
    return SaveCasaCommand(**casa_properties)


def update_casa_cmd(casa_id, **casa_properties):
    """
    Command to update Casa entity with id equals 'casa_id'
    :param casa_properties: a dict of properties to update model
    :return: a Command that update Casa, validating and localizing properties received as strings
    """
    return UpdateCasaCommand(casa_id, **casa_properties)


def list_casas_cmd():
    """
    Command to list Casa entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListCasaCommand()


def casa_form(**kwargs):
    """
    Function to get Casa's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return CasaForm(**kwargs)


def get_casa_cmd(casa_id):
    """
    Find casa by her id
    :param casa_id: the casa id
    :return: Command
    """
    return GetCasaCommand(casa_id)



def delete_casa_cmd(casa_id):
    """
    Construct a command to delete a Casa
    :param casa_id: casa's id
    :return: Command
    """
    return DeleteCasaCommand(casa_id)

