# Generated by Django 4.0.3 on 2022-03-26 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MidtermApp', '0026_remove_account_statement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='ssn',
            field=models.CharField(max_length=9),
        ),
    ]