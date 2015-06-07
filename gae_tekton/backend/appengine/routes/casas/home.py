# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from casa_app import casa_facade
from routes.casas import new, edit
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index():
    cmd = casa_facade.list_casas_cmd()
    casas = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    casa_form = casa_facade.casa_form()

    def localize_casa(casa):
        casa_dct = casa_form.fill_with_model(casa)
        casa_dct['edit_path'] = router.to_path(edit_path, casa_dct['id'])
        casa_dct['delete_path'] = router.to_path(delete_path, casa_dct['id'])
        return casa_dct

    localized_casas = [localize_casa(casa) for casa in casas]
    context = {'casas': localized_casas,
               'new_path': router.to_path(new)}
    return TemplateResponse(context, 'casas/casa_home.html')


def delete(casa_id):
    casa_facade.delete_casa_cmd(casa_id)()
    return RedirectResponse(router.to_path(index))

