# Generated by Django 3.2.9 on 2021-12-04 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('placements', '0002_auto_20211204_1908'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='email',
            new_name='emailid',
        ),
    ]