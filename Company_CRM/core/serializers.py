from django import forms
from rest_framework import serializers

from Company_CRM.company.models import Company
from Company_CRM.employee.models import Employee


class ShortCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name',)


class ShortEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name')


class EmployeeSerializer(serializers.ModelSerializer):
    company = ShortCompanySerializer()
    photo = serializers.ImageField(
        required=False,
        use_url=True)

    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        company_name = validated_data.pop('company').get('name')
        try:
            company = Company.objects.filter(name=company_name).get()
        except Company.DoesNotExist:
            company = Company.objects.create(name=company_name)
        return Employee.objects.create(**validated_data, company=company)


    def update(self, instance, validated_data):
        company_name = validated_data.pop('company').get('name')
        try:
            company = Company.objects.filter(name=company_name).get()
        except Company.DoesNotExist:
            company = Company.objects.create(name=company_name)
        return Employee.objects.create(**validated_data, company=company)


class CompanySerializer(serializers.ModelSerializer):
    employee_set = ShortEmployeeSerializer(many=True, read_only=True)
    logo = serializers.ImageField(
        required=False,
        use_url=True)

    class Meta:
        model = Company
        fields = '__all__'

    # def create(self, validated_data):
    #     return super().create(validated_data)
