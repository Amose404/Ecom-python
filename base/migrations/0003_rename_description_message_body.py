# Generated by Django 3.2.12 on 2023-01-06 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20230106_1741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='description',
            new_name='body',
        ),
    ]
