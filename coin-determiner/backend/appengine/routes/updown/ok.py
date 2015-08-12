# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from routes.updown import download
from tekton.router import to_path
from gaepermission.decorator import login_not_required
from google.appengine.ext.blobstore.blobstore import BlobInfo
import logging

from coin import CoinDeterminer

@login_not_required
@no_csrf
def index(blob_key):
    input_numbers = BlobInfo.get(blob_key).open().read().split()
    output_numbers = [CoinDeterminer(num) for num in input_numbers]


    context = {'download_path': to_path(download, blob_key=blob_key), 'input': input_numbers, 'output': output_numbers}
    return TemplateResponse(context, 'updown/ok.html')
