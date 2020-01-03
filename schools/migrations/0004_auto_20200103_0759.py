# Generated by Django 3.0.1 on 2020-01-03 07:59

from django.db import migrations
import json
from django.contrib.gis.geos import fromstr
from pathlib import Path

DATA_FILENAME = 'residential_area_data.json'


def load_data(apps, schema_editor):
    ResidentialArea = apps.get_model('schools', 'ResidentialArea')
    jsonfile = Path(__file__).parents[2] / DATA_FILENAME

    with open(str(jsonfile)) as datafile:
        objects = json.load(datafile)
        for obj in objects['elements']:
            try:
                objType = obj['type']
                if objType == 'node':
                    tags = obj['tags']
                    name = tags.get('name', 'no-name')
                    longitude = obj.get('lon', 0)
                    latitude = obj.get('lat', 0)
                    location = fromstr(
                        f'POINT({longitude} {latitude})', srid=4326
                    )
                    ResidentialArea(name=name, location=location).save()
            except KeyError:
                pass
class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0003_residentialarea'),
    ]

    operations = [
    ]