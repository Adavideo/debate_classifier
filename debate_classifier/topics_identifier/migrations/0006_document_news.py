# Generated by Django 3.0.3 on 2020-08-02 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics_identifier', '0005_auto_20200731_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='news',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]