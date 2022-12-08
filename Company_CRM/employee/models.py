from django.core import validators
from django.db import models
from Company_CRM.company.models import Company
from Company_CRM.core.validators.model_validators import only_letters_validator, max_file_size_validator_to_5MB


class Employee(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 40
    POSITION_MAX_LENGTH = 50

    SALARY_MIN_VALUE = 0

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(validators.MinLengthValidator(FIRST_NAME_MIN_LENGTH),
                    only_letters_validator,),
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(validators.MinLengthValidator(LAST_NAME_MIN_LENGTH),
                    only_letters_validator,),
        null=False,
        blank=False,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    photo = models.ImageField(
        upload_to='employees_photos/',
        validators=(max_file_size_validator_to_5MB,),
        null=True,
        blank=True,
    )

    position = models.CharField(
        max_length=POSITION_MAX_LENGTH,
        null=False,
        blank=False,
    )

    salary = models.FloatField(
        validators=(validators.MinValueValidator(SALARY_MIN_VALUE),),
        null=False,
        blank=False,
    )

    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
