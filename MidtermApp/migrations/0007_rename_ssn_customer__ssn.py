# Generated by Django 4.0.3 on 2022-03-14 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MidtermApp', '0006_alter_customer_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='ssn',
            new_name='_ssn',
        ),
    ]
