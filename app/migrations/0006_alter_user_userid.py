# Generated by Django 4.2 on 2023-05-13 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userid',
            field=models.CharField(max_length=50, unique=True, verbose_name='유저ID'),
        ),
    ]