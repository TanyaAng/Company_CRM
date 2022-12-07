from django.urls import path

from Company_CRM.employee.views import ListEmployeeApiView, DetailsEmployeeApiView

urlpatterns = (
    path('', ListEmployeeApiView.as_view(), name='api list employee'),
    path('<int:pk>/', DetailsEmployeeApiView.as_view(), name='api details employee'),

)
