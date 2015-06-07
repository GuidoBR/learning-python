# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from casa_app import casa_facade
from routes import casas
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index(casa_id):
    casa = casa_facade.get_casa_cmd(casa_id)()
    casa_form = casa_facade.casa_form()
    context = {'save_path': router.to_path(save, casa_id), 'casa': casa_form.fill_with_model(casa)}
    return TemplateResponse(context, 'casas/casa_form.html')


def save(casa_id, **casa_properties):
    cmd = casa_facade.update_casa_cmd(casa_id, **casa_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors, 'casa': casa_properties}

        return TemplateResponse(context, 'casas/casa_form.html')
    return RedirectResponse(router.to_path(casas))

