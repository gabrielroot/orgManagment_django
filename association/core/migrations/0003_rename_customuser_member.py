# Generated by Django 4.0.2 on 2022-02-28 21:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_alter_customuser_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomUser',
            new_name='Member',
        ),
    ]
