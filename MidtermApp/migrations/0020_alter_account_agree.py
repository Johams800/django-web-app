# Generated by Django 4.0.3 on 2022-03-26 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MidtermApp', '0019_account_agree_alter_transaction_transaction_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='agree',
            field=models.BooleanField(),
        ),
    ]
