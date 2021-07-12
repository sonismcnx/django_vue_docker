# Generated by Django 3.2.3 on 2021-07-12 10:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210712_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='stars',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
