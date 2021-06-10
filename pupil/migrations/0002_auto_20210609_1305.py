# Generated by Django 3.2.4 on 2021-06-09 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0001_initial'),
        ('pupil', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pupil',
            name='subject',
        ),
        migrations.AddField(
            model_name='pupil',
            name='subject',
            field=models.ManyToManyField(to='subject.Subject'),
        ),
    ]
