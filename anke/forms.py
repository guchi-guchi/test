from django.forms import ModelForm, TextInput, Textarea, Select
from anke.models import Anke


class AnkeForm(ModelForm):

    class Meta:
        model = Anke
        exclude = ('user',)
        fields = ('name', 'address', 'email', 'question1', 'question2','question3')
        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'フルネームで記入して下さい',
            }),
            'address': TextInput(attrs={
                'placeholder': 'できるだけ詳しく記入して下さい',
            }),
            'email': TextInput(attrs={
                'placeholder': '普段ご利用のEメールアドレスをご入力ください',
            }),
            'question1': Textarea(attrs={
                'placeholder': '自由に記入して下さい',
            }),
            'question2': TextInput(attrs={
                'placeholder': '数字を入力して下さい',
            }),
            'question3': Select(attrs={
                'placeholder': '選択してください',
            }),
        }
        labels = {
            'name': 'お名前',
            'address': 'ご住所',
            'email': 'Eメールアドレス',
            'question1': '質問①：耳納北麓エリアで一番好きな所は（例：施設、お店、風景など）？',
            'question2': '質問②：このエリアに来る前に、比較した場所があったら教えてください。',
            'question3': '質問③：ここまでの移動手段を教えてください。',
        }