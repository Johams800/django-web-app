# Generated by Django 4.0.3 on 2022-03-26 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MidtermApp', '0023_alter_account_security_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='statement',
            field=models.CharField(default='', max_length=3),
        ),
    ]