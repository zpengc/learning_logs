# Generated by Django 3.0.3 on 2020-02-25 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_auto_20200225_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
