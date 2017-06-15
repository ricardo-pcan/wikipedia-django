# -*- coding: utf-8 -*-
from django.core.management import call_command
from django.core.urlresolvers import reverse

from redsep_offline.meds.models import Med

from rest_framework import status
from rest_framework.test import APITestCase


class MedTests(APITestCase):

    def setUp(self):
        call_command('loaddata', 'types.json', verbosity=0)

    def create_med(self):
        return Med.objects.create(
            title="med", description="description", type_class_id=1
        )

    def test_med_list(self):
        med = self.create_med()
        endpoint_url = reverse('api:v1:meds-list')
        response = self.client.get(endpoint_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['id'], med.id)
        self.assertEqual(response.data['results'][0]['title'], med.title)
        self.assertEqual(
            response.data['results'][0]['description'], med.description
        )

    def test_med_retrieve(self):
        med = self.create_med()
        endpoint_url = reverse('api:v1:meds-detail', kwargs={'pk': med.id})
        response = self.client.get(endpoint_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], med.id)
        self.assertEqual(response.data['title'], med.title)
        self.assertEqual(response.data['description'], med.description)
