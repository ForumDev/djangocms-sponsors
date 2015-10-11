# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('url', models.TextField(default=b'')),
                ('image', models.ImageField(upload_to=b'images/sponsor/', verbose_name=b'Spnsor image')),
                ('sites', models.ManyToManyField(to='sites.Site')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
