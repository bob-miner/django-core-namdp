# Generated by Django 5.1.4 on 2025-01-15 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_management', '0002_permission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='users',
            field=models.ManyToManyField(db_table='user_permission', to='event_management.authuserapi'),
        ),
    ]
