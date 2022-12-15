from rest_framework import status
from rest_framework import generics as api_views
from rest_framework import views as rest_base_views
from rest_framework.response import Response

from Company_CRM.core.repository.employee_repository import get_all_employees, get_employee
from Company_CRM.core.serializers import EmployeeSerializer


class ListEmployeeApiView(api_views.ListCreateAPIView):
    queryset = get_all_employees()
    serializer_class = EmployeeSerializer


# class ListEmployeeApiView(rest_base_views.APIView):
#     def get(self, request):
#         employees = get_all_employees()
#         serializer = EmployeeSerializer(employees)
#         return Response({"employees": serializer.data})
#
#     def post(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailsEmployeeApiView(rest_base_views.APIView):
    def get(self, request, pk):
        employee = get_employee(pk)
        serializer = EmployeeSerializer(employee)
        return Response(data=serializer.data)

    def put(self, request, pk):
        employee = get_employee(pk)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = get_employee(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
