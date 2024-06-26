# Generated by Django 5.0 on 2024-03-27 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcapp', '0002_rename_mail_datas_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('service', models.CharField(max_length=100)),
                ('day', models.IntegerField()),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='datas',
            name='phone_number',
            field=models.CharField(default='', max_length=20),
        ),
    ]
