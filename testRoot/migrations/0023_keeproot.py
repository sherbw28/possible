# Generated by Django 4.0.2 on 2022-02-15 12:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testRoot', '0022_typeofplace_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeepRoot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('first', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='first', to='testRoot.typeofplace')),
                ('second', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second', to='testRoot.typeofplace')),
                ('third', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='third', to='testRoot.typeofplace')),
            ],
        ),
    ]