# Generated by Django 5.2 on 2025-04-23 21:48

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geo_pos', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]
