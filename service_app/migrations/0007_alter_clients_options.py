# Generated by Django 4.1.3 on 2022-11-06 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0006_rename_client_clients_rename_service_services'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clients',
            options={'ordering': ['-client_name']},
        ),
    ]