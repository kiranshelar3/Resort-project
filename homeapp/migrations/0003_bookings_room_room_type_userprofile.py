# Generated by Django 3.2.7 on 2021-12-02 07:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0002_auto_20210712_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='room_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.CharField(max_length=15)),
                ('cost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='userProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('status', models.IntegerField(default=1)),
                ('no', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.IntegerField()),
                ('room_status', models.BooleanField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeapp.room_type')),
            ],
        ),
        migrations.CreateModel(
            name='booKings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin_date', models.DateField(blank=True, default=datetime.datetime(2021, 12, 2, 12, 44, 52, 109437))),
                ('chekout_date', models.DateField()),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeapp.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeapp.userprofile')),
            ],
        ),
    ]
