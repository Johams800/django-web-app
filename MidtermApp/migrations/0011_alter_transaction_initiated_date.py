# Generated by Django 4.0.3 on 2022-03-19 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MidtermApp', '0010_alter_transaction_initiated_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='initiated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
