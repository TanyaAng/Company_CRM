from django.contrib import admin

from Company_CRM.company.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass
