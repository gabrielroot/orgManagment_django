# Generated by Django 4.0.2 on 2022-03-01 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_remove_member_vehicle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='message',
        ),
    ]
