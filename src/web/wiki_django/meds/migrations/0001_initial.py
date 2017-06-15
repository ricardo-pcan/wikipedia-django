# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import redsep_offline.meds.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date', null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified', null=True)),
                ('name', models.CharField(max_length=600)),
                ('position', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('is_oficial', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=500, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Bloque',
                'verbose_name_plural': 'Bloques',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date', null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified', null=True)),
                ('name', models.CharField(max_length=600)),
                ('position', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('is_oficial', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=500, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Grado',
                'verbose_name_plural': 'Grados',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date', null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified', null=True)),
                ('name', models.CharField(max_length=600)),
                ('position', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('is_oficial', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=500, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Nivel',
                'verbose_name_plural': 'Niveles',
            },
        ),
        migrations.CreateModel(
            name='Med',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date', null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified', null=True)),
                ('title', models.CharField(max_length=600)),
                ('description', models.TextField(null=True, verbose_name='descripci\xf3n', blank=True)),
                ('thumbnail', models.ImageField(max_length=400, null=True, upload_to=redsep_offline.meds.models.get_thumbnail_path, blank=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('original_id', models.BigIntegerField(null=True, verbose_name='ID original', blank=True)),
                ('donated_by', models.CharField(default=b'', max_length=256, verbose_name='donated by')),
                ('reference_url', models.URLField(max_length=500, null=True, verbose_name='reference url', blank=True)),
                ('donor_website', models.URLField(max_length=500, null=True, verbose_name='donor website', blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Recurso digital',
                'verbose_name_plural': 'Recursos digitales',
            },
        ),
        migrations.CreateModel(
            name='MedSubType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date', null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified', null=True)),
                ('name', models.CharField(max_length=600, verbose_name=b'name')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'is active')),
                ('description', models.CharField(max_length=300, null=True, blank=True)),
                ('slug', models.SlugField(max_length=600)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Subtipo de recurso digital',
                'verbose_name_plural': 'Subtipos de recursos digitales',
            },
        ),
        migrations.CreateModel(
            name='MedType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date', null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified', null=True)),
                ('name', models.CharField(max_length=600, verbose_name=b'name')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'is active')),
                ('description', models.CharField(max_length=300, null=True, blank=True)),
                ('slug', models.SlugField(max_length=600)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Tipo de recurso digital',
                'verbose_name_plural': 'Tipos de recursos digitales',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date', null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified', null=True)),
                ('attached_file', models.FileField(upload_to=redsep_offline.meds.models.get_resource_path, max_length=400, verbose_name=b'file')),
                ('attached_file_size', models.PositiveIntegerField(default=0, verbose_name=b'file size')),
                ('format_file', models.CharField(max_length=45, null=True, blank=True)),
                ('uncompressed_directory', models.CharField(max_length=500, null=True, verbose_name=b'uncompressed directory', blank=True)),
                ('is_flash', models.BooleanField(default=False, verbose_name=b'is flash')),
                ('med', models.ForeignKey(related_name='resources', to='meds.Med')),
            ],
            options={
                'verbose_name': 'Recurso',
                'verbose_name_plural': 'Recursos',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date', null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified', null=True)),
                ('name', models.CharField(max_length=600)),
                ('position', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('is_oficial', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=500, null=True, blank=True)),
                ('grade', models.ForeignKey(related_name='subjects', to='meds.Grade')),
            ],
            options={
                'verbose_name': 'Materia',
                'verbose_name_plural': 'Materias',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date', null=True)),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified', null=True)),
                ('name', models.CharField(max_length=600)),
                ('position', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('is_oficial', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=500, null=True, blank=True)),
                ('block', models.ForeignKey(related_name='themes', to='meds.Block')),
            ],
            options={
                'verbose_name': 'Tema',
                'verbose_name_plural': 'Temas',
            },
        ),
        migrations.AddField(
            model_name='medsubtype',
            name='med_type',
            field=models.ForeignKey(related_name='subtypes', blank=True, to='meds.MedType', null=True),
        ),
        migrations.AddField(
            model_name='med',
            name='subtype',
            field=models.ForeignKey(blank=True, to='meds.MedSubType', null=True),
        ),
        migrations.AddField(
            model_name='med',
            name='themes',
            field=models.ManyToManyField(to='meds.Theme'),
        ),
        migrations.AddField(
            model_name='med',
            name='type_class',
            field=models.ForeignKey(related_name='meds', to='meds.MedType'),
        ),
        migrations.AddField(
            model_name='grade',
            name='level',
            field=models.ForeignKey(related_name='grades', to='meds.Level'),
        ),
        migrations.AddField(
            model_name='block',
            name='subject',
            field=models.ForeignKey(related_name='blocks', to='meds.Subject'),
        ),
    ]
