from django import forms
from rest_framework import serializers

from Company_CRM.company.models import Company
from Company_CRM.core.repository.company_repository import get_company_by_name, check_if_company_exist_by_name
from Company_CRM.core.validators.serializers_validators import get_or_create_company_by_name
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

    def is_valid(self, *args, **kwargs):
        print(self.initial_data)
        company = self.initial_data.get('company')
        if company:
            company_name = company.get('name')
            get_or_create_company_by_name(company_name)
        return super().is_valid(*args, **kwargs)

    def create(self, validated_data):
        company_name = validated_data.pop('company').get('name')
        company = get_company_by_name(company_name)
        return Employee.objects.create(**validated_data, company=company)

    def update(self, instance, validated_data):
        print(validated_data)
        company = validated_data.get('company')

        if company:
            company_name = validated_data.pop('company').get('name')
            instance.company = get_company_by_name(company_name)


        for key, value in validated_data.items():
            if key != 'company' and value:
                setattr(instance, key, value)
        instance.save()
        return instance


class CompanySerializer(serializers.ModelSerializer):
    employee_set = ShortEmployeeSerializer(many=True, read_only=True)
    logo = serializers.ImageField(
        required=False,
        use_url=True)

    class Meta:
        model = Company
        fields = '__all__'

    def create(self, validated_data):
        company_name = validated_data.get('name')
        if check_if_company_exist_by_name(company_name):
            raise serializers.ValidationError('Company with this name already exists.')
        return Company.objects.create(**validated_data)
