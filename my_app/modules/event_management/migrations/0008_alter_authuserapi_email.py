# Generated by Django 5.1.4 on 2025-01-12 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_management', '0007_authuserapi_alter_event_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuserapi',
            name='email',
            field=models.CharField(max_length=150),
        ),
    ]
