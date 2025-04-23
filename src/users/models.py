import json

from django.contrib.gis.db import models


class User(models.Model):
    geo_pos = models.PointField()

    # Django Ninja does not natively support GeoDjango's custom fields: https://github.com/vitalik/django-ninja/issues/335
    @property
    def geo_pos_geometry(self):
        return json.loads(self.geo_pos.json)
