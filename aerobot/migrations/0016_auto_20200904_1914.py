# Generated by Django 3.1 on 2020-09-04 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aerobot', '0015_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='link',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]
