# Generated by Django 4.0.3 on 2022-03-20 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MidtermApp', '0013_alter_account_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='agreement',
            field=models.TextField(default='Unless otherwise defined in this Agreement or the context requires otherwise, words and expressions used in this Agreement have the meanings and instructions ascribed to them in the Master Definitions Schedule set out in Schedule 1 of the draft Incorporated Terms Memorandum which will be executed and dated on or about the date of this Agreement and signed for the purpose of identification by the parties to this Agreement and others (as the same may be amended, varied and supplemented from time to time with the consent of the parties to this Agreement, the “Incorporated Terms Memorandum”). This Agreement shall be construed in accordance with the principles of construction and interpretation set out in such Master Definitions Schedule.'),
        ),
    ]
