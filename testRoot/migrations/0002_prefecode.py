# Generated by Django 4.0.2 on 2022-02-04 03:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testRoot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrefeCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(47)])),
            ],
        ),
    ]