# Generated by Django 2.2.10 on 2020-04-27 01:18

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200425_0506'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='image',
            field=models.ImageField(null=True, upload_to=core.models.drug_image_file_path),
        ),
    ]