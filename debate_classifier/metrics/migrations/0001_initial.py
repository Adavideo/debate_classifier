# Generated by Django 3.0.3 on 2020-10-13 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('timeline', '0003_threadtopic_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicAnnotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.BooleanField()),
                ('annotator', models.IntegerField()),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timeline.Thread')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timeline.Topic')),
            ],
        ),
    ]
