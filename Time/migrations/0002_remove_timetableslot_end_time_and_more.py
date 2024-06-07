# Generated by Django 5.0.6 on 2024-06-07 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Time', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetableslot',
            name='end_time',
        ),
        migrations.AlterField(
            model_name='timetableslot',
            name='start_time',
            field=models.CharField(choices=[('08:30', '08:30 - 10:00'), ('10:10', '10:10 - 11:40'), ('11:50', '11:50 - 13:20'), ('13:30', '13:30 - 15:00'), ('15:10', '15:10 - 16:40')], max_length=10),
        ),
    ]
