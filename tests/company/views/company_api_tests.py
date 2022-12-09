import json

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from Company_CRM.company.models import Company
from Company_CRM.core.serializers import CompanySerializer

client = Client()


class CompanyViewTests(TestCase):
    def setUp(self):
        Company.objects.create(name='Microsoft')
        Company.objects.create(name='Google')

        self.valid_company = {
            "name": "Facebook"
        }

        self.invalid_company = {
            "name": "Microsoft"
        }

    def get_all_listed_companies(self):
        response = client.get(reverse('api list company'))
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def create_invalid_company_entity(self):
        response = client.post(reverse('api list company'),
                               data=json.dumps(self.invalid_company),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def get_valid_company_entity(self):
        response = client.get(reverse('api details company', kwargs={'pk': 1}))
        company = Company.objects.get(pk=1)
        serializer = CompanySerializer(company)
        self.assertEqual(response.data,
                         serializer.data)

    def get_invalid_company_entity(self):
        response = client.get(reverse('api details company', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def update_valid_company_entity(self):
        response = client.post(reverse('api details company', kwargs={'pk': 1}),
                               data=json.dumps(self.valid_company),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
