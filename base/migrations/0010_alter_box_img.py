# Generated by Django 3.2.13 on 1980-01-04 23:39

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_box_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='img',
            field=models.ImageField(null=True, upload_to=base.models.user_directory_path),
        ),
    ]