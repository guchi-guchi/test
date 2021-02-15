from django.forms import *
from anke.models import *


class AnkeForm(ModelForm):

    class Meta:
        model = Anke
        fields = ('name', 'shop', 'gender', 'age', 'address', 'email', 'question1', 'question2', 'question3', 'question4', 'question5', 'question6', 'question7', 'question8', 'question9', 'question10', 'question11', 'question12', 'question13', 'question14', 'question15', 'notification')
        question3 = ModelChoiceField(queryset=Traffic.objects.all())
        question4 = ModelMultipleChoiceField(queryset=Person.objects.all())
        question5 = ModelMultipleChoiceField(queryset=Purpose.objects.all())
        question6 = ModelMultipleChoiceField(queryset=Media.objects.all())
        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'フルネームで記入して下さい',
            }),
            'shop': Select(attrs={
                'placeholder': '選択して下さい',
            }),
            'gender': Select(attrs={
                'placeholder': '選択して下さい',
            }),
            'age': Select(attrs={
                'placeholder': '数字を記入して下さい',
            }),
            'address': TextInput(attrs={
                'placeholder': '市町村名までで結構です',
            }),
            'email': EmailInput(attrs={
                'placeholder': '普段ご利用のEメールアドレスをご入力ください',
            }),
            'question1': Select(attrs={
                'placeholder': '数字を入力してください。',
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
            'question6': CheckboxSelectMultiple(attrs={
                'placeholder': '選択してください',
            }),
            'question7': TextInput(attrs={
                'placeholder': '自由に記入して下さい',
            }),
            'question8': Select(attrs={
                'placeholder': '金額の数字を入力してください',
            }),
            'question9': Select(attrs={
                'placeholder': '金額の数字を入力してください',
            }),
            'question10': TextInput(attrs={
                'placeholder': '自由に記入して下さい',
            }),
            'question11': TextInput(attrs={
                'placeholder': '自由に記入して下さい',
            }),
            'question12': TextInput(attrs={
                'placeholder': '自由に記入して下さい',
            }),
            'question13': NumberInput(attrs={
                'placeholder': '数字を入力してください',
            }),
            'question14': TextInput(attrs={
                'placeholder': '自由に記入して下さい',
            }),
            'question15': TextInput(attrs={
                'placeholder': '自由に記入して下さい',
            }),
            'notification': CheckboxInput(attrs={
                'placeholder': '自由に記入して下さい',
            }),
        }
        labels = {
            'name': 'お名前',
            'shop': 'ご来店の店舗名',
            'gender': '性別',
            'age': 'ご年代',
            'address': 'ご住所',
            'email': 'Eメールアドレス',
            'question1': '質問1：耳納北麓エリアに来るのは何回目ですか？',
            'question2': '質問2：このエリアに来る前に、比較した場所があったら教えてください。',
            'question3': '質問3：本日の移動手段は？',
            'question4': '質問4：本日は、どなたとご一緒ですか？(複数選択可)。',
            'question5': '質問5：本日の主な目的は？(複数選択可)。',
            'question6': '質問6：何をご覧になって来られましたか？(複数選択可)',
            'question7': '質問7：この後耳納北麓エリア以外に訪れる予定の場所があれば、ご記入ください。',
            'question8': '質問8：耳納北麓エリアで食事に使う費用はいくらですか？',
            'question9': '質問9：耳納北麓エリアで土産など買い物に使う費用はいくらですか？',
            'question10': '質問10：耳納北麓エリアで一番好きなところは？（例：施設、お店、風景など）',
            'question11': '質問11：このエリアに来ると決めた理由は何ですか？',
            'question12': '質問12：今まで旅行した中で、一番好きだった場所はどこですか？',
            'question13': '質問13：その場所が100点とすると、このエリアは何点ですか？',
            'question14': '質問14：その点数にした（減点した）理由は何ですか？',
            'question15': '質問15：このエリアに欠けてるものがあるとすれば、それは何でしょうか？',
            'notification': '<span class="text-success lead">久留米ＤＭＯメールマガジンの<br>購読</span><br><span class="text-danger">ご希望の方は左上のボックスをタップして<br>チェックを付けてください。</span>',
        }
