# Generated by Django 4.0.3 on 2022-03-26 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MidtermApp', '0021_account_paper_statement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(default='Completed', max_length=10),
        ),
    ]
