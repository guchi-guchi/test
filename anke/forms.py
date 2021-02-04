from django.forms import ModelForm, TextInput, Textarea, Select, EmailInput, RadioSelect, NumberInput
from anke.models import Anke


class AnkeForm(ModelForm):

    class Meta:
        model = Anke
        exclude = ('user',)
        fields = ('name', 'shop', 'sex', 'age', 'address', 'email', 'question1', 'question2','question3')
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
            'question3': RadioSelect(attrs={
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
            'question3': '質問③：ここまでの移動手段を教えてください。',
        }