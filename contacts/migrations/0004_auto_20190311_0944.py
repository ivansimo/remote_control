# Generated by Django 2.1.5 on 2019-03-11 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20190222_1053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='nombrecontacto',
        ),
    ]
