# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from mimetypes import MimeTypes
from zipfile import ZipFile

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from redsep_offline.meds.models import Med, MedType, Resource, Theme


class Command(BaseCommand):
    "Import resources for zip"

    args = '<archivo__zip>'
    help = 'Import med resources from ZIP file, '

    mandatory_fields = [
        "id", "title", "description", "curricular_alignment",
        "type", "thumbnail", "resources",
        "donated_by", "donor_website", "reference_url"
    ]

    def handle(self, *args, **options):
        if len(args) == 1:
            if args[0].endswith(".zip"):
                zip_path = args[0]
                self.parse(zip_path)
                created_meds = self.create(zip_path)
                self.stdout.write(
                    "SUCCESS: %d meds created" % created_meds
                )
            else:
                self.stdout.write("ERROR: Wrong extension file")

        else:
            self.stdout.write("ERROR: Wrong number of arguments")

    def parse(self, zip_path):
        archive = ZipFile(zip_path, 'r')
        data = json.loads(archive.read("data.json"))

        # Loop data and check required fields
        for item in data:
            if not all(field in item for field in self.mandatory_fields):
                self.stdout.write(
                    ("ERROR: Required fields:")
                )
                self.stdout.write(",".join(self.mandatory_fields))
                exit()

    def create(self, zip_path):
        archive = ZipFile(zip_path, 'r')
        created_meds = 0
        data = json.loads(archive.read("data.json"))

        # Loop data
        for item in data:
            med_type = MedType.objects.get(name=item['type'])
            med, created = Med.objects.get_or_create(
                original_id=item['id'],
                defaults={
                    'title': item['title'],
                    'description': item['description'],
                    'type_class': med_type,
                    'donated_by': item['donated_by'],
                    'donor_website': item['donor_website'],
                    'reference_url': item['reference_url']
                }
            )

            if created:
                # Save thumbnails
                med.thumbnail.save(
                    item["thumbnail"],
                    ContentFile(archive.read(item['thumbnail']))
                )

                # Save resources
                for resource_path in item["resources"]:
                    resource = Resource(med=med)
                    resource.attached_file.save(
                        resource_path,
                        ContentFile(archive.read(resource_path))
                    )
                    mime = MimeTypes()
                    resource.format_file = (
                        mime.guess_type(resource.attached_file.url)[0]
                    )
                    resource.attached_file_size = resource.attached_file.size
                    resource.save()

                # Save themes in med
                for theme_dict in item['curricular_alignment']:
                    try:
                        theme = Theme.objects.get(id=theme_dict['theme'])
                    except Theme.DoesNotExist:
                        continue

                    med.themes.add(theme)

                created_meds += 1

        return created_meds
