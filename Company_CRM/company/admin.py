from django.contrib import admin

from Company_CRM.employee.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    pass
