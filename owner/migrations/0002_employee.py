# Generated by Django 4.0.1 on 2022-02-08 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=120)),
                ('employee_designation', models.CharField(max_length=120)),
                ('employee_experience', models.PositiveIntegerField()),
                ('employee_salary', models.PositiveIntegerField()),
            ],
        ),
    ]
