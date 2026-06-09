from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.validators import RegexValidator

from .models import ExpenseRecord

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = ExpenseRecord
        fields = ['category', 'amount', 'description', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.TextInput(attrs={'placeholder': '例如：午餐、車資、訂閱費'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault('class', 'form-control')

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount is None or amount <= 0:
            raise forms.ValidationError("金額必須是大於 0 的整數。")
        return int(amount)


class BootstrapLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control form-control-lg'
    
class CustomRegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='使用者名稱',
        help_text='僅限英文字母與數字',
        validators=[RegexValidator(r'^[a-zA-Z0-9]*$', '僅限字母與數字')],
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control form-control-lg'})
            field.widget.attrs.update({'placeholder': f'請輸入{field.label}'})

        self.fields['password1'].label = '密碼'
        self.fields['password2'].label = '密碼確認'
        self.fields['password1'].help_text = '至少 4 個字元，且需含至少一個英文字母'
        self.fields['password2'].help_text = ''