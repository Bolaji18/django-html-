# Generated by Django 4.1.6 on 2023-03-12 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_infos_joined_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=800)),
                ('lastname', models.CharField(max_length=500)),
                ('nin', models.CharField(max_length=500)),
                ('homeaddress', models.CharField(max_length=500)),
                ('phone_no', models.CharField(max_length=500)),
                ('dob', models.CharField(max_length=500)),
            ],
        ),
    ]
