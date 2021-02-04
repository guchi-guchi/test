# Generated by Django 3.1.6 on 2021-02-04 03:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Anke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='氏名')),
                ('address', models.CharField(blank=True, max_length=300, null=True, verbose_name='住所')),
                ('email', models.EmailField(max_length=254, verbose_name='Eメールアドレス')),
                ('question1', models.TextField(blank=True, null=True, verbose_name='質問①')),
                ('question2', models.CharField(blank=True, max_length=200, null=True, verbose_name='質問②')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='回答日時')),
                ('status', models.CharField(choices=[('on', 'オンライン'), ('off', '紙')], default='on', max_length=200, null=True, verbose_name='回答手段')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='anke_created', to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
            options={
                'verbose_name': 'アンケート',
                'verbose_name_plural': 'アンケート',
            },
        ),
    ]
