# Generated by Django 4.2.5 on 2023-09-27 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description_6',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]