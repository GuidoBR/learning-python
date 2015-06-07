# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from casa_app import casa_facade


@login_not_required
@no_csrf
def index():
    cmd = casa_facade.list_casas_cmd()
    casas = cmd()

    def localize_casa(casa):
        casa_form = casa_facade.casa_form()
        casa_dct = casa_form.fill_with_model(casa)
        return casa_dct

    localized_casas = [localize_casa(casa) for casa in casas]
    context = {'casas': localized_casas}

    return TemplateResponse(context)
