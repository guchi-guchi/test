# Generated by Django 3.1.6 on 2021-02-04 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anke', '0004_auto_20210204_2255'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anke',
            options={'permissions': [('special_status1', 'kapateria')], 'verbose_name': 'アンケート', 'verbose_name_plural': 'アンケート'},
        ),
    ]
