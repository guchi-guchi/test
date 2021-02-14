from django.contrib import admin
from anke.models import *

def notify(modeladmin, request, queryset):
    for post in queryset:
        post.email_push(request)


class AnkeAdmin(admin.ModelAdmin):
    model = Anke
    list_display = ('name','shop', 'sex', 'age', 'email')


class NewsletterAdmin(admin.ModelAdmin):
    model = Newsletter
    actions = [notify]


admin.site.register(Traffic)
admin.site.register(Person)
admin.site.register(Purpose)
admin.site.register(Media)
admin.site.register(Anke, AnkeAdmin)
admin.site.register(Newsletter, NewsletterAdmin)

notify.short_description = 'メルマガを配信する'
admin.site.site_header = "久留米DMOアンケートサイト"
admin.site.index_title = '入力・編集画面'                
admin.site.site_title = '久留米DMOアンケート：管理サイト' 