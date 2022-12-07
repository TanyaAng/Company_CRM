from rest_framework import status
from rest_framework import generics as api_views
from rest_framework.response import Response
from rest_framework import views as rest_base_views

from Company_CRM.core.repository.company_repository import get_all_companies, get_company
from Company_CRM.core.serializers import CompanySerializer


class ListCompanyApiView(api_views.ListCreateAPIView):
    queryset = get_all_companies()
    serializer_class = CompanySerializer


# class ListCompanyApiView(APIView):
#     def get(self, request):
#         employees = get_all_companies()
#         serializer = CompanySerializer(employees)
#         return Response({"employees": serializer.data})
#
#     def post(self, request):
#         serializer = CompanySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailsCompanyApiView(rest_base_views.APIView):
    def get(self, request, pk):
        company = get_company(pk)
        serializer = CompanySerializer(company)
        return Response(data=serializer.data)

    def post(self, request, pk):
        company = get_company(pk)
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        company = get_company(pk)
        company.delete()
        return Response(status=status.HTTP_201_CREATED)

