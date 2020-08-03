# Generated by Django 3.0.3 on 2020-08-03 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0002_document'),
        ('topics_identifier', '0009_auto_20200803_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cluster',
            name='reference_document',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='timeline.Document'),
        ),
        migrations.AlterField(
            model_name='clusterdocument',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timeline.Document'),
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]