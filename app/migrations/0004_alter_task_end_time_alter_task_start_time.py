# Generated by Django 4.1.2 on 2023-03-14 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_task_end_time_alter_task_start_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
    ]
