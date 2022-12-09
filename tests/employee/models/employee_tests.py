from django.core.exceptions import ValidationError
from django.test import TestCase

from Company_CRM.company.models import Company
from Company_CRM.employee.models import Employee


class EmployeeModelTests(TestCase):

    def test_employee_save__when_names_are_valid__expect_correct(self):
        company = Company(name='Google')
        company.full_clean()
        company.save()

        employee = Employee(
            first_name='Tanya',
            last_name='Angelova',
            position='Engineer',
            salary=1200,
            company=company
        )

        employee.full_clean()
        employee.save()

        self.assertIsNotNone(employee.pk)

    def test_employee_save__when_first_name_is_not_valid__expect_exception(self):
        company = Company(name='Google')
        company.full_clean()
        company.save()

        employee = Employee(
            first_name='Tanya2',
            last_name='Angelova',
            position='Engineer',
            salary=1200,
            company=company
        )

        with self.assertRaises(ValidationError) as context:
            employee.full_clean()
            employee.save()

        self.assertIsNotNone(context.exception)

    def test_employee_save__when_last_name_is_not_valid__expect_exception(self):
        company = Company(name='Google')
        company.full_clean()
        company.save()

        employee = Employee(
            first_name='Tanya',
            last_name='Ange_lova',
            position='Engineer',
            salary=1200,
            company=company
        )

        with self.assertRaises(ValidationError) as context:
            employee.full_clean()
            employee.save()

        self.assertIsNotNone(context.exception)
