# Generated by Django 3.2.21 on 2023-09-20 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20230920_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='max_value',
            field=models.PositiveIntegerField(default=100),
        ),
        migrations.AddField(
            model_name='habit',
            name='value',
            field=models.PositiveIntegerField(default=0),
        ),
    ]