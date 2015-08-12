# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import logging
from routes.updown import ok
from tekton import router
from tekton.gae.middleware.redirect import RedirectResponse
from gaepermission.decorator import login_not_required


@login_not_required
def index(_handler, files):
    blob_infos = _handler.get_uploads('files[]')
    path = router.to_path(ok, blob_key=blob_infos[0].key())
    return RedirectResponse(path) 
