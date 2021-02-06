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
        verbose_name = ('質問３（交通手段）')
        verbose_name_plural = ('質問３（交通手段）')


class Person(models.Model):
    name = models.CharField(max_length=255, verbose_name=('同伴者'))
    slug = models.SlugField(unique=True, verbose_name=('スラグ'))
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name=('作成日時'))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ('質問４（人物）')
        verbose_name_plural = ('質問４（人物）')


class Purpose(models.Model):
    name = models.CharField(max_length=255, verbose_name=('目的'))
    slug = models.SlugField(unique=True, verbose_name=('スラグ'))
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name=('作成日時'))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ('質問５（目的）')
        verbose_name_plural = ('質問５（目的）')


class Media(models.Model):
    name = models.CharField(max_length=255, verbose_name=('メディア種別'))
    slug = models.SlugField(unique=True, verbose_name=('スラグ'))
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name=('作成日時'))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ('質問６（メディア）')
        verbose_name_plural = ('質問６（メディア）')



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
        ('others', 'その他'),
    )

    SEX_CHOICES = (
        ('m', '男性'),
        ('f', '女性'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='anke_created',
                             on_delete=models.PROTECT, verbose_name=('ユーザー'), null=True, blank=True)
    name = models.CharField(max_length=200, verbose_name=('氏名'))
    shop = models.CharField(max_length=300, default='others', verbose_name=('お店'), choices=SHOP_CHOICES)
    age = models.PositiveIntegerField(null=True, verbose_name=('年齢'), blank=True)
    sex = models.CharField(max_length=200, verbose_name=('性別'), choices=SEX_CHOICES, default='f')
    address = models.CharField(blank=True, null=True, max_length=300, verbose_name=('住所'))
    email = models.EmailField(verbose_name=('Eメールアドレス'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=('回答日時'), null=True)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, verbose_name='回答手段', null=True, default='on')
    question1 = models.PositiveIntegerField(blank=True, null=True, verbose_name=('質問1'))
    question2 = models.CharField(max_length=300, blank=True, null=True, verbose_name=('質問2'))
    question3 = models.ForeignKey(Traffic, on_delete=models.PROTECT, verbose_name='質問3', blank=True, null=True)
    question4 = models.ManyToManyField(Person, verbose_name='質問4', blank=True)
    question5 = models.ManyToManyField(Purpose, verbose_name='質問5', blank=True)
    question6 = models.ManyToManyField(Media, verbose_name='質問6', blank=True)
    question7 = models.CharField(max_length=300, blank=True, null=True, verbose_name=('質問7'))
    question8 = models.PositiveIntegerField(blank=True, null=True, verbose_name=('質問8'))
    question9 = models.PositiveIntegerField(blank=True, null=True, verbose_name=('質問9'))
    question10 = models.CharField(max_length=300, blank=True, null=True, verbose_name=('質問10'))
    question11 = models.TextField(blank=True, null=True, verbose_name=('質問11'))
    question12 = models.CharField(max_length=300, blank=True, null=True, verbose_name=('質問12'))
    question13 = models.PositiveIntegerField(blank=True, null=True, verbose_name=('質問13'))
    question14 = models.TextField(blank=True, null=True, verbose_name=('質問14'))
    question15 = models.TextField(blank=True, null=True, verbose_name=('質問15'))


    class Meta:
        verbose_name = ('アンケート')
        verbose_name_plural = ('アンケート')
        permissions = [
            ('special_status1', 'kapateria'),
        ]

    def __str__(self):
        return self.name