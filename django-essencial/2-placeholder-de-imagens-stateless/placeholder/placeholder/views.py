import hashlib
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import etag
from django.shortcuts import render
from placeholder.placeholder import ImageForm


def index(request):
    return render(request, 'home.html')


def generate_etag(request, width, height):
    content = 'Placeholder: {} x {}'.format(width, height)
    return hashlib.sha1(content.encode('utf-8')).hexdigest()


@etag(generate_etag)
def placeholder(request, width, height):
    form = ImageForm({'width': width, 'height': height})
    if form.is_valid():
        image = form.generate()
        return HttpResponse(image, content_type='image/png')
    else:
        return HttpResponseBadRequest('Invalid dimensions')
