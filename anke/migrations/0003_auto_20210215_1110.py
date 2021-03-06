# Generated by Django 3.1.6 on 2021-02-15 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anke', '0002_auto_20210214_1826'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anke',
            options={'ordering': ['-created'], 'verbose_name': 'アンケート', 'verbose_name_plural': 'アンケート'},
        ),
        migrations.AlterField(
            model_name='anke',
            name='notification',
            field=models.BooleanField(default=False, null=True, verbose_name='メルマガ'),
        ),
    ]
