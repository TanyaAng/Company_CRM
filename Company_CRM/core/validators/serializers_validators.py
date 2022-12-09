from django.core.exceptions import ObjectDoesNotExist
from Company_CRM.core.repository.company_repository import get_company_by_name, create_company_with_name


def get_or_create_company_by_name(name):
    try:
        company = get_company_by_name(name)
    except ObjectDoesNotExist:
        company = create_company_with_name(name)
    return company
