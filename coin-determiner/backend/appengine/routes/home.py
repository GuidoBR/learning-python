# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from google.appengine.api.app_identity.app_identity import get_default_gcs_bucket_name
from google.appengine.ext.blobstore import blobstore
from tekton import router
from routes.updown import upload


@login_not_required
@no_csrf
def index():
    """
    Upload file to Google Cloud Storage
    """
    success_url = router.to_path(upload)
    bucket = get_default_gcs_bucket_name()
    url = blobstore.create_upload_url(success_url, gs_bucket_name=bucket)
    context = {'upload_url': url}
    return TemplateResponse(context, 'home.html')
