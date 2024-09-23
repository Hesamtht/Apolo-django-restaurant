# Generated by Django 5.0.7 on 2024-09-04 22:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('body', models.TextField(verbose_name='نظر')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ اضافه شدن')),
                ('active', models.BooleanField(default=False)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.food')),
            ],
        ),
    ]
