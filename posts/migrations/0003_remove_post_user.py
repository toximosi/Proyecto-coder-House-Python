# Generated by Django 4.0.4 on 2022-05-07 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_user_bio_remove_user_birthdate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]