from Company_CRM.employee.models import Employee


def get_all_employees():
    return Employee.objects.all()


def get_all_employees_of_company(company_pk):
    employees = Employee.objects.filter(company=company_pk)
    return employees


def get_employee(pk):
    employee = Employee.objects.filter(id=pk)
    if employee:
        return employee.get()
    return None
