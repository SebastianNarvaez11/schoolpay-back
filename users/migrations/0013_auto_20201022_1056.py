# Generated by Django 2.2.3 on 2020-10-22 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20200906_1636'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['last_name'], 'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
    ]
