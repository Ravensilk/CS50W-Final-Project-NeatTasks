# Generated by Django 4.2.4 on 2023-11-14 05:08

import boards.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_boards_background_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boards',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to=boards.models.Boards.board_image_path),
        ),
    ]
