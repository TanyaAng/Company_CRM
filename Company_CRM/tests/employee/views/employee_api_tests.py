import json

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from Company_CRM.company.models import Company
from Company_CRM.core.serializers import EmployeeSerializer
from Company_CRM.employee.models import Employee

client = Client()


class EmployeeViewTests(TestCase):

    def setUp(self):
        microsoft = Company.objects.create(name='Microsoft')
        google = Company.objects.create(name='Google')
        Employee.objects.create(first_name='Tanya', last_name='Angelova', position='Engineer',
                                salary=3500, company=microsoft)
        Employee.objects.create(first_name='George', last_name='Petrov', position='Team Lead',
                                salary=12000, company=google)

        self.valid_employee = {
            "company": {
                "name": "Microsoft"
            },
            "first_name": "Tanya",
            "last_name": "Angelova",
            "position": "Junior Software Engineer",
            "salary": 2500,
        }

        self.invalid_employee = {
            "company": {
                "name": "Microsoft"
            },
            "first_name": "Marina2",
            "last_name": "Petrova",
            "position": "Junior",
            "salary": 1800,
        }

    def test_get_all_listed_employees__expect_to_be_successful(self):
        response = client.get(reverse('api list employee'))
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_employee__when_valid_entity__expect_to_be_successful(self):
        response = client.get(reverse('api details employee', kwargs={'pk': 1}))
        employee = Employee.objects.get(pk=1)
        serializer = EmployeeSerializer(employee)
        self.assertEqual(response.data, serializer.data)

    def test_get_employee__when_invalid_entity__expect_not_found(self):
        response = client.get(reverse('api details employee', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_employee__when_valid_entity__expect_to_be_created(self):
        response = client.post(
            reverse('api details employee', kwargs={'pk': 1}),
            data=json.dumps(self.valid_employee),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_employee__when_invalid_entity__expect_bad_request(self):
        response = client.post(
            reverse('api details employee', kwargs={'pk': 1}),
            data=json.dumps(self.invalid_employee),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
