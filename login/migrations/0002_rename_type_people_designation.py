# Generated by Django 4.1.3 on 2023-04-17 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='type',
            new_name='designation',
        ),
    ]