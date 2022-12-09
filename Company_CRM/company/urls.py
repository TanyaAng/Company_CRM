from django.urls import path

from Company_CRM.company.views import ListCompanyApiView, DetailsCompanyApiView

urlpatterns = (
    path('', ListCompanyApiView.as_view(), name='api list company' ),
    path('<int:pk>/', DetailsCompanyApiView.as_view(), name='api details company'),


)