from django.contrib import admin
from django.urls import path, include

urlpatterns = (
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/',
         include([
             path('company/', include('Company_CRM.company.urls')),
             path('employee/', include('Company_CRM.employee.urls'))
         ]),
         ))
