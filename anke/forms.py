from django.forms import *
from anke.models import *


class AnkeForm(ModelForm):

    class Meta:
        model = Anke
        exclude = ('user',)
        fields = ('name', 'shop', 'sex', 'age', 'address', 'email', 'question1', 'question2', 'question3', 'question4', 'question5', 'question6')
        question3 = ModelChoiceField(queryset=Traffic.objects.all())
        question4 = ModelMultipleChoiceField(queryset=Person.objects.all())
        question5 = ModelMultipleChoiceField(queryset=Purpose.objects.all())
        question6 = ModelChoiceField(queryset=Media.objects.all())
        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'フルネームで記入して下さい',
            }),
            'shop': Select(attrs={
                'placeholder': '選択して下さい',
            }),
            'sex': RadioSelect(attrs={
                'placeholder': '選択して下さい',
            }),
            'age': NumberInput(attrs={
                'placeholder': '数字を記入して下さい',
            }),
            'address': TextInput(attrs={
                'placeholder': '市町村名までで結構です',
            }),
            'email': EmailInput(attrs={
                'placeholder': '普段ご利用のEメールアドレスをご入力ください',
            }),
            'question1': TextInput(attrs={
                'placeholder': '自由に記入して下さい',
            }),
            'question2': TextInput(attrs={
                'placeholder': '自由に記入して下さい',
            }),
            'question3': Select(attrs={
                'placeholder': '選択してください',
            }),
            'question4': CheckboxSelectMultiple(attrs={
                'placeholder': '選択してください',
            }),
            'question5': CheckboxSelectMultiple(attrs={
                'placeholder': '選択してください',
            }),
            'question6': Select(attrs={
                'placeholder': '選択してください',
            }),
        }
        labels = {
            'name': 'お名前',
            'shop': '現在ご来店の場所',
            'sex': '性別',
            'age': 'ご年齢',
            'address': 'ご住所',
            'email': 'Eメールアドレス',
            'question1': '質問①：耳納北麓エリアで一番好きな所は？（例：施設、お店、風景など）',
            'question2': '質問②：このエリアに来る前に、比較した場所があったら教えてください。',
            'question3': '質問③：本日の移動手段は？',
            'question4': '質問④：本日は、どなたとご一緒ですか？(複数選択可)。',
            'question5': '質問⑤：本日の主な目的は？(複数選択可)。',
            'question6': '質問⑥：何をご覧になって来られましたか？',
        }
