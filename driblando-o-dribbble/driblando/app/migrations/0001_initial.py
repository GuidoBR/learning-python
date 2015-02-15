# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nome', models.CharField(max_length=50)),
                ('foto', models.CharField(max_length=140)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Shots',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('titulo', models.CharField(max_length=140)),
                ('imagem', models.CharField(max_length=200)),
                ('conteudo', models.CharField(max_length=500)),
                ('autor', models.ForeignKey(to='app.Autor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
