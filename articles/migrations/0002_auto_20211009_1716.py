# Generated by Django 3.2.8 on 2021-10-09 16:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default='nada'),
            preserve_default=False,
        ),
    ]