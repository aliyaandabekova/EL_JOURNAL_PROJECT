# Generated by Django 3.2.4 on 2021-06-10 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0003_alter_pupil_avg_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='pupil',
            name='photo',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]