# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from casa_app import casa_facade


def index():
    cmd = casa_facade.list_casas_cmd()
    casa_list = cmd()
    casa_form = casa_facade.casa_form()
    casa_dcts = [casa_form.fill_with_model(m) for m in casa_list]
    return JsonResponse(casa_dcts)


def new(_resp, **casa_properties):
    cmd = casa_facade.save_casa_cmd(**casa_properties)
    return _save_or_update_json_response(cmd, _resp)


def edit(_resp, id, **casa_properties):
    cmd = casa_facade.update_casa_cmd(id, **casa_properties)
    return _save_or_update_json_response(cmd, _resp)


def delete(_resp, id):
    cmd = casa_facade.delete_casa_cmd(id)
    try:
        cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)


def _save_or_update_json_response(cmd, _resp):
    try:
        casa = cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)
    casa_form = casa_facade.casa_form()
    return JsonResponse(casa_form.fill_with_model(casa))

