# Generated by Django 3.2.4 on 2021-06-09 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pupil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Алия', max_length=30)),
                ('avg_score', models.PositiveIntegerField(default=0)),
                ('subject', models.ManyToManyField(to='subject.Subject')),
            ],
        ),
        migrations.AlterField(
            model_name='score',
            name='pupil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.pupil'),
        ),
    ]
