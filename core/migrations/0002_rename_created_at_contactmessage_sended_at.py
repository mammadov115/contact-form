# Generated by Django 5.2.4 on 2025-07-15 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactmessage',
            old_name='created_at',
            new_name='sended_at',
        ),
    ]
