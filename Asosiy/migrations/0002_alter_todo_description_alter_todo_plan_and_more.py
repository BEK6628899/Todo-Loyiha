# Generated by Django 4.1.7 on 2023-02-17 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Asosiy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='todo',
            name='plan',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Talaba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('st_raqam', models.CharField(max_length=10)),
                ('kurs', models.PositiveSmallIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='todo',
            name='Talaba',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Asosiy.talaba'),
        ),
    ]
