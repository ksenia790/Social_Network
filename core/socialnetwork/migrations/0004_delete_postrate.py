# Generated by Django 4.0.4 on 2022-06-01 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialnetwork', '0003_post_dislikes_post_likes_postrate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PostRate',
        ),
    ]
