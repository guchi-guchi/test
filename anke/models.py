from django.db import models
from django.utils import timezone
from django.conf import settings


class Anke(models.Model):
    
    STATUS_CHOICES = (
        ('on', 'オンライン'),
        ('off', '紙'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='anke_created',
                             on_delete=models.PROTECT, verbose_name=('ユーザー'), null=True, blank=True)
    name = models.CharField(max_length=200, verbose_name=('氏名'))
    address = models.CharField(blank=True, null=True, max_length=300, verbose_name=('住所'))
    email = models.EmailField(verbose_name=('Eメールアドレス'))
    question1 = models.TextField(blank=True, null=True, verbose_name=('質問①'))
    question2 = models.CharField(max_length=200, blank=True, null= True, verbose_name=('質問②'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=('回答日時'), null=True)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, verbose_name='回答手段', null=True, default='on')

    class Meta:
        verbose_name = ('アンケート')
        verbose_name_plural = ('アンケート')

    def __str__(self):
        return self.name