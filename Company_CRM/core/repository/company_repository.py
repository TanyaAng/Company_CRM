from django.http import Http404
from rest_framework import serializers

from Company_CRM.company.models import Company


def get_all_companies():
    return Company.objects.all()


def get_company(pk):
    company = Company.objects.filter(id=pk)
    if company:
        return company.get()
    raise Http404


def get_company_by_name(name):
    return Company.objects.filter(name=name).get()


def create_company_with_name(name):
    return Company.objects.create(name=name)


def check_if_company_exist_by_name(name):
    if Company.objects.filter(name=name):
        return True
    return False

