from django.contrib import admin
from anke.models import *

def notify(modeladmin, request, queryset):
    for post in queryset:
        post.email_push(request)


class AnkeAdmin(admin.ModelAdmin):
    model = Anke
    list_display = ('name','shop', 'gender', 'age', 'email', 'notification')
    list_filter = ('shop', 'gender', 'age', 'notification', 'status')
    search_fields = ('name', 'email', 'address', )


class NewsletterAdmin(admin.ModelAdmin):
    model = Newsletter
    list_display = ('title','created',)
    actions = [notify]


admin.site.register(Traffic)
admin.site.register(Person)
admin.site.register(Purpose)
admin.site.register(Media)
admin.site.register(Anke, AnkeAdmin)
admin.site.register(Newsletter, NewsletterAdmin)

notify.short_description = 'メルマガを配信する'
admin.site.site_header = "久留米DMOアンケート：管理サイト"
admin.site.index_title = '編集画面'                
admin.site.site_title = '久留米DMOアンケート：管理サイト' 