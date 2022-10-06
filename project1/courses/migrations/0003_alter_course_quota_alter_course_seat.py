# Generated by Django 4.1.1 on 2022-10-04 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_quota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='quota',
            field=models.CharField(choices=[('OPEN', 'OPEN'), ('CLOSED', 'CLOSED')], default='OPEN', max_length=64),
        ),
        migrations.AlterField(
            model_name='course',
            name='seat',
            field=models.PositiveIntegerField(default=99),
        ),
    ]
