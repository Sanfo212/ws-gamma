# Generated by Django 3.2.7 on 2021-10-11 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20211009_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.TextField(default='nada'),
            preserve_default=False,
        ),
    ]