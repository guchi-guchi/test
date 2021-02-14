from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


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

    VISIT_CHOICES = (
        ('0', '初めて'),
        ('1', '２回目〜５回目'),
        ('2', '６回目〜１０回目'),
        ('3', '１０回以上'),
        ('4', '地元住民'),
    )
    
    MONEY_CHOICES = (
        ('0', '1000円未満'),
        ('1', '1000円以上〜2000円未満'),
        ('2', '2000円以上〜3000円未満'),
        ('3', '4000円以上〜5000円未満'),
        ('4', '5000円以上〜10000円未満'),
        ('5', '10000円以上'),
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

    name = models.CharField(max_length=200, verbose_name=('氏名'))
    shop = models.CharField(max_length=300, default='others', verbose_name=('お店'), choices=SHOP_CHOICES)
    age = models.PositiveIntegerField(null=True, verbose_name=('年齢'), blank=True)
    sex = models.CharField(max_length=200, verbose_name=('性別'), choices=SEX_CHOICES, default='f')
    address = models.CharField(blank=True, null=True, max_length=300, verbose_name=('住所'))
    email = models.EmailField(verbose_name=('Eメールアドレス'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=('回答日時'), null=True)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, verbose_name='回答手段', null=True, default='on')
    question1 = models.CharField(max_length=300, blank=True, choices=VISIT_CHOICES, default='0', verbose_name=('質問1'))
    question2 = models.CharField(max_length=300, blank=True, null=True, verbose_name=('質問2'))
    question3 = models.ForeignKey(Traffic, on_delete=models.PROTECT, verbose_name='質問3', blank=True, null=True)
    question4 = models.ManyToManyField(Person, verbose_name='質問4', blank=True)
    question5 = models.ManyToManyField(Purpose, verbose_name='質問5', blank=True)
    question6 = models.ManyToManyField(Media, verbose_name='質問6', blank=True)
    question7 = models.CharField(max_length=300, blank=True, null=True, verbose_name=('質問7'))
    question8 = models.CharField(max_length=300, blank=True, choices=MONEY_CHOICES, default='0', verbose_name=('質問8'))
    question9 = models.CharField(max_length=300, blank=True, choices=MONEY_CHOICES, default='0', verbose_name=('質問9'))
    question10 = models.CharField(max_length=300, blank=True, null=True, verbose_name=('質問10'))
    question11 = models.TextField(blank=True, null=True, verbose_name=('質問11'))
    question12 = models.CharField(max_length=300, blank=True, null=True, verbose_name=('質問12'))
    question13 = models.PositiveIntegerField(blank=True, null=True, verbose_name=('質問13'))
    question14 = models.TextField(blank=True, null=True, verbose_name=('質問14'))
    question15 = models.TextField(blank=True, null=True, verbose_name=('質問15'))
    notification = models.BooleanField(default=True, null=True, verbose_name=('通知'))

    class Meta:
        verbose_name = ('アンケート')
        verbose_name_plural = ('アンケート')

    def __str__(self):
        return self.name

    
class Newsletter(models.Model):
    title = models.CharField(max_length=300, null=True, verbose_name=('タイトル'))
    message = models.TextField(verbose_name=('本文'))

    class Meta:
        verbose_name = ('メールマガジン')
        verbose_name_plural = ('メールマガジン')

    def __str__(self):
        return self.title

    def email_push(self, request):
        context = {
            'news': self,
        }
        subject = render_to_string('anke/notify_subject.txt', context, request)
        message = render_to_string('anke/notify_message.txt', context, request)

        from_email = settings.DEFAULT_FROM_EMAIL
        bcc = [settings.DEFAULT_FROM_EMAIL]
        for mail_push in Anke.objects.filter(notification=True):
            bcc.append(mail_push.email)
        email = EmailMessage(subject, message, from_email, [], bcc)
        email.send()