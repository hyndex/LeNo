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
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_content', models.TextField(blank=True, null=True)),
                ('publish_date', models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 5, 22, 52, 15, 677257), null=True)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 5, 22, 52, 15, 677257), null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group', to='users.Group')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='media.Media')),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notification.Notification')),
            ],
        ),
    ]