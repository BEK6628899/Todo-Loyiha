# Generated by Django 4.1.7 on 2023-02-17 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asosiy', '0003_alter_todo_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
