from django.db import models
from django.utils import timezone
from django.conf import settings


class Traffic(models.Model):
    name = models.CharField(max_length=255, verbose_name=('交通手段'))
    slug = models.SlugField(unique=True, verbose_name=('スラグ'))
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name=('作成日時'))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ('交通')
        verbose_name_plural = ('交通')



class Anke(models.Model):
    
    STATUS_CHOICES = (
        ('on', 'オンライン'),
        ('off', '紙'),
    )

    SHOP_CHOICES = (
        ('ka', 'カパテリア'),
        ('be', '紅乙女酒造'),
        ('ky', '巨峰ワイン'),
        ('ju', '樹蘭マルシェ'),
    )

    SEX_CHOICES = (
        ('m', '男性'),
        ('f', '女性'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='anke_created',
                             on_delete=models.PROTECT, verbose_name=('ユーザー'), null=True, blank=True)
    name = models.CharField(max_length=200, verbose_name=('氏名'))
    shop = models.CharField(max_length=300, null=True, verbose_name=('お店'), choices=SHOP_CHOICES)
    age = models.PositiveIntegerField(null=True, verbose_name=('年齢'))
    sex = models.CharField(max_length=200, null=True, verbose_name=('性別'), choices=SEX_CHOICES)
    address = models.CharField(blank=True, null=True, max_length=300, verbose_name=('住所'))
    email = models.EmailField(verbose_name=('Eメールアドレス'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=('回答日時'), null=True)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, verbose_name='回答手段', null=True, default='on')
    question1 = models.TextField(blank=True, null=True, verbose_name=('質問①'))
    question2 = models.TextField(blank=True, null=True, verbose_name=('質問②'))
    question3 = models.ManyToManyField(Traffic, max_length=200, verbose_name='質問③', blank=True)

    class Meta:
        verbose_name = ('アンケート')
        verbose_name_plural = ('アンケート')
        permissions = [
            ('special_status1', 'kapateria'),
        ]

    def __str__(self):
        return self.name