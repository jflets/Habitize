# Generated by Django 3.2.21 on 2023-11-14 10:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_alter_habit_goal_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='goal_amount',
            field=models.PositiveIntegerField(default=10, validators=[django.core.validators.MaxValueValidator(9999)]),
        ),
    ]
