# Generated by Django 3.2.7 on 2021-10-04 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plant',
            old_name='date_posted',
            new_name='date_added',
        ),
        migrations.RenameField(
            model_name='plant',
            old_name='title',
            new_name='name',
        ),
    ]
