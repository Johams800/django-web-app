# Generated by Django 4.0.3 on 2022-03-26 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MidtermApp', '0022_alter_transaction_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='security_code',
            field=models.CharField(max_length=50),
        ),
    ]
