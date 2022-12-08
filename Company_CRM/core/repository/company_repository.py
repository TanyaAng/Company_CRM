from django.http import Http404

from Company_CRM.company.models import Company


def get_all_companies():
    return Company.objects.all()


def get_company(pk):
    company = Company.objects.filter(id=pk)
    if company:
        return company.get()
    raise Http404
