# Generated by Django 3.0.3 on 2020-08-02 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics_identifier', '0006_document_news'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='news',
            new_name='is_news',
        ),
    ]