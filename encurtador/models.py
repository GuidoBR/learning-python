from django.db import models

class Link(models.Model):
    url = models.URLField()

    @staticmethod
    def shorten(url_original):
        return "h"
