# Generated by Django 5.0 on 2024-03-27 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcapp', '0003_appointment_alter_datas_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='service',
            new_name='services',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='day',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='month',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='year',
            field=models.CharField(max_length=4),
        ),
    ]
