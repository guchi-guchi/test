from django.forms import *
from anke.models import Anke


class AnkeForm(ModelForm):

    class Meta:
        model = Anke
        exclude = ('user',)
        fields = ('name', 'address', 'email', 'question1', 'question2',)
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
        }
        labels = {
            'name': 'お名前',
            'address': 'ご住所',
            'email': 'Eメールアドレス',
            'question1': '質問①：このブログの感想を教えて下さい',
            'question2': '質問②：このブログは１００点満点中の何点ですか？',
        }