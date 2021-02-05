from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail, send_mass_mail, BadHeaderError
from anke.models import Anke
from anke.forms import AnkeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import permission_required
from django.views.generic import ListView, DetailView
import csv
import io
import urllib

@login_required 
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
            message1 = (subject, f"「{subject}」さまがアンケートに回答されました。", from_email, ['kurumedmo@gmail.com'])
            message2 = (subject, f"「{subject}」 さま \n ご回答ありがとうございます。\n 特設ページはこちらです→ http://127.0.0.1:8000/gift/ \n ", from_email, [from_email])
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


class AnkeKapaList(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Anke
    queryset = Anke.objects.filter(shop='ka')
    template_name = 'anke/ka_list.html'
    context_object_name = 'data'
    permission_required = 'anke.special_status1'


@staff_member_required
def ankeExport(request):
    data = Anke.objects.all()
    
    response = HttpResponse(content_type='text/csv; charset=Shift-JIS')
    filename = urllib.parse.quote((u'アンケート回答リスト.csv').encode("utf8"))
    response['Content-Disposition'] = 'attachment; filename*=UTF-8\'\'{}'.format(filename)
    writer = csv.writer(response)
    writer.writerow(['回答日', 'ID', '手段', '氏名', '住所', 'Eメールアドレス', '質問１', '質問２', '質問３'])
    for answer in data:
        writer.writerow([answer.created, answer.user, answer.status, answer.name, answer.address, answer.email, answer.question1, answer.question2, answer.question3.all()])
    return response


@permission_required('anke.special_status1')
@login_required
def ankeKapaExport(request):
    data = Anke.objects.filter(shop='ka')
    response = HttpResponse(content_type='text/csv; charset=Shift-JIS')
    filename = urllib.parse.quote((u'アンケート回答リスト_カパテリア.csv').encode("utf8"))
    response['Content-Disposition'] = 'attachment; filename*=UTF-8\'\'{}'.format(filename)
    writer = csv.writer(response)
    writer.writerow(['回答日', '手段', '店舗', '性別', '年齢', '質問１', '質問２', '質問３'])
    for answer in data:
        writer.writerow([answer.created, answer.status, answer.shop, answer.sex, answer.age , answer.question1, answer.question2, answer.question3.all()])
    return response

@login_required
def giftView(request):
    return render(request, 'anke/gift.html')

@login_required
def tableView(request):
    return render(request, 'anke/table.html')
