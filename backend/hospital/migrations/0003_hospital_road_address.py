# Generated by Django 4.2.7 on 2024-02-01 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_alter_hospital_call'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='road_address',
            field=models.TextField(blank=True),
        ),
    ]
