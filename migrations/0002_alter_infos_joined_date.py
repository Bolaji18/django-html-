# Generated by Django 4.1.6 on 2023-03-12 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infos',
            name='joined_date',
            field=models.DateField(null=True),
        ),
    ]
