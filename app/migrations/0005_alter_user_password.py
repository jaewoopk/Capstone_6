# Generated by Django 4.2 on 2023-05-13 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_sentencedata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100, verbose_name='비밀번호'),
        ),
    ]
