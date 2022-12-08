# Generated by Django 4.1.4 on 2022-12-08 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_alter_company_name'),
        ('employee', '0003_alter_employee_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company'),
        ),
    ]