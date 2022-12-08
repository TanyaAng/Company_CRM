from django.db import models

from Company_CRM.core.validators.model_validators import max_file_size_validator_to_5MB


class Company(models.Model):
    NAME_MAX_LENGTH = 40
    DESCRIPTION_MAX_LENGTH = 300

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
    )

    logo = models.ImageField(
        upload_to='company_logos/',
        validators=(max_file_size_validator_to_5MB,),
        null=True,
        blank=True,
    )

    description = models.TextField(
        max_length=DESCRIPTION_MAX_LENGTH,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
