from django.contrib import admin
from anke.models import Anke

class AnkeAdmin(admin.ModelAdmin):
    model = Anke
    list_display = ('name','shop', 'sex', 'age', 'address', 'email')
    
    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        obj.save()
        super(AnkeAdmin, self).save_model(request, obj, form, change)

admin.site.register(Anke, AnkeAdmin)

admin.site.site_header = "久留米DMOアンケートサイト"
admin.site.index_title = '入力・編集画面'                
admin.site.site_title = '久留米DMOアンケート：管理サイト' 