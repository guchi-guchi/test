from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail, send_mass_mail, BadHeaderError
from anke.models import Anke
from anke.forms import AnkeForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required

import csv
import io
import urllib

def index(request):
    return render(request, "anke/index.html")

def ankeView(request):
    params ={'message': '', 'form': None}
    if request.method == 'POST':
        form = AnkeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            message1 = (f"アンケート回答のお知らせ。「{name}」さま", f"「{name}」さまがアンケートに回答されました。", from_email, ['s-shotaro@berraquera-jp.com'])
            message2 = ("アンケート回答のお礼", f"「{name}」 さま \n ご回答ありがとうございます。\n\nJR田主丸駅構内のカフェ「カパテリア」で「400円分サービス」させていただきます。 \n\nご利用の際はスタッフにこのメールをお見せください。", from_email, [from_email])
            try:
                send_mass_mail((message1, message2), fail_silently=False)
            except BadHeaderError:
                return HttpResponse('無効なヘッダーが見つかりました。')
            survey = form.save(commit=False)
            survey = form.save()
            form.save_m2m()
            return redirect('anke:index')
        else:
            params['message'] = '再入力して下さい'
            params['form'] = form
    else:
        params['form'] = AnkeForm()
    return render(request, 'anke/survey.html', params)


@staff_member_required
@login_required
def ankeList(request):
    data = Anke.objects.all()
    return render(request, 'anke/list.html', {'data': data})


@staff_member_required
def ankeExport(request):
    data = Anke.objects.all()
    response = HttpResponse(content_type='text/csv; charset=Shift-JIS')
    filename = urllib.parse.quote((u'アンケート回答リスト.csv').encode("utf8"))
    response['Content-Disposition'] = 'attachment; filename*=UTF-8\'\'{}'.format(filename)
    writer = csv.writer(response)
    writer.writerow(['回答日', '手段', '氏名', '住所', '年代', '性別', 'Eメールアドレス', '質問１', '質問２', '質問３', '質問４', '質問５', '質問６', '質問7', '質問8', '質問9', '質問10', '質問11', '質問12', '質問13', '質問14', '質問15'])
    for answer in data:
        writer.writerow([answer.created.date(), answer.status, answer.name, answer.address, answer.age, answer.gender, answer.email, answer.question1, answer.question2, answer.question3, answer.question4.all(), answer.question5.all(), answer.question6.all(), answer.question7, answer.question8, answer.question9, answer.question10, answer.question11, answer.question12, answer.question13, answer.question14, answer.question15])
    return response

@staff_member_required
def tableView(request):
    return render(request, 'anke/table.html')
