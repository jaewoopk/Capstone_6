# Generated by Django 3.2.10 on 2023-04-27 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SentenceData',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]