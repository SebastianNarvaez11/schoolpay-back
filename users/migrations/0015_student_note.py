# Generated by Django 2.2.3 on 2021-04-23 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20210421_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='note',
            field=models.CharField(default='', max_length=200, verbose_name='Nota'),
        ),
    ]