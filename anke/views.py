from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail, send_mass_mail, BadHeaderError
from anke.models import Anke
from anke.forms import AnkeForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import permission_required
from django.views.generic import ListView, DetailView
import csv
import io
import urllib

def index(request):
    return render(request, "anke/index.html")

@login_required 
def ankeView(request):
    params ={'message': '', 'form': None}
    if request.method == 'POST':
        form = AnkeForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            message1 = (subject, f"「{subject}」さまがアンケートに回答されました。", from_email, ['s-shotaro@berraquera-jp.com'])
            message2 = (subject, f"「{subject}」 さま \n ご回答ありがとうございます。\n 特設ページはこちらです→ https://kurumedmo-survey.herokuapp.com/gift/ \n ", from_email, [from_email])
            try:
                send_mass_mail((message1, message2), fail_silently=False)
            except BadHeaderError:
                return HttpResponse('無効なヘッダーが見つかりました。')
            survey = form.save(commit=False)
            survey.user = request.user
            survey.save()
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


@permission_required('anke.special_status1')
@login_required
def ankeList_ka(request):
    data = Anke.objects.filter(shop='ka')
    return render(request, 'anke/ka_list.html', {'data': data})


@staff_member_required
def ankeExport(request):
    data = Anke.objects.all()
    response = HttpResponse(content_type='text/csv; charset=Shift-JIS')
    filename = urllib.parse.quote((u'アンケート回答リスト.csv').encode("utf8"))
    response['Content-Disposition'] = 'attachment; filename*=UTF-8\'\'{}'.format(filename)
    writer = csv.writer(response)
    writer.writerow(['回答日', 'ID', '手段', '氏名', '住所', 'Eメールアドレス', '質問１', '質問２', '質問３', '質問４', '質問５', '質問６', '質問7', '質問8', '質問9', '質問10', '質問11', '質問12', '質問13', '質問14', '質問15'])
    for answer in data:
        writer.writerow([answer.created, answer.user, answer.status, answer.name, answer.address, answer.email, answer.question1, answer.question2, answer.question3, answer.question4.all(), answer.question5.all(), answer.question6.all(), answer.question7, answer.question8, answer.question9, answer.question10, answer.question11, answer.question12, answer.question13, answer.question14, answer.question15])
    return response


@permission_required('anke.special_status1')
@login_required
def ankeKapaExport(request):
    data = Anke.objects.filter(shop='ka')
    response = HttpResponse(content_type='text/csv; charset=Shift-JIS')
    filename = urllib.parse.quote((u'アンケート回答リスト_カパテリア.csv').encode("utf8"))
    response['Content-Disposition'] = 'attachment; filename*=UTF-8\'\'{}'.format(filename)
    writer = csv.writer(response)
    writer.writerow(['回答日', 'ID', '手段', '氏名', '住所', 'Eメールアドレス', '質問１', '質問２', '質問３', '質問４', '質問５', '質問６', '質問7', '質問8', '質問9', '質問10', '質問11', '質問12', '質問13', '質問14', '質問15'])
    for answer in data:
        writer.writerow([answer.created, answer.user, answer.status, answer.name, answer.address, answer.email, answer.question1, answer.question2, answer.question3, answer.question4.all(), answer.question5.all(), answer.question6.all(), answer.question7, answer.question8, answer.question9, answer.question10, answer.question11, answer.question12, answer.question13, answer.question14, answer.question15])
    return response

@login_required
def giftView(request):
    return render(request, 'anke/gift.html')

@login_required
def tableView(request):
    return render(request, 'anke/table.html')
