# Generated by Django 2.2.6 on 2019-10-05 17:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0006_auto_20191005_2252'),
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, null=True)),
                ('description', models.TextField(default='', null=True)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
                ('date_updated', models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 5, 22, 52, 15, 664875))),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Institute')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.Profile')),
                ('media', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='media.Media')),
            ],
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='', null=True)),
                ('description', models.TextField(default='', null=True)),
                ('date_updated', models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 5, 22, 52, 15, 665912))),
                ('media', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='media.Media')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_updated', models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 5, 22, 52, 15, 665912))),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Options')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Question')),
            ],
        ),
    ]