# Generated by Django 4.1.7 on 2023-03-28 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='zipcode',
            new_name='postal_code',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='state',
            new_name='province',
        ),
    ]
