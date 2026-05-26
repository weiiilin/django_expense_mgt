from django import forms
from .models import ExpenseRecord
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = ExpenseRecord
        # 我們只需要讓使用者填這四個，user 和 created_at 會自動處理
        fields = ['category', 'amount', 'description', 'date']
        

    # 自定義驗證：金額必須大於 0
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        # 改為整數判斷
        if amount is None or amount <= 0:
            raise forms.ValidationError("金額必須是大於 0 的整數。")
        return int(amount) # 強制轉為 int 確保萬無一失
    
class CustomRegistrationForm(UserCreationForm):
    # 這裡的 label 不要加冒號
    username = forms.CharField(
        label="使用者名稱", 
        help_text="僅限字母、數字",
        validators=[RegexValidator(r'^[a-zA-Z0-9]*$', '僅限字母與數字')],
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # --- 自動化修復區 ---
        for field_name, field in self.fields.items():
            # 1. 強制幫所有欄位加上 form-control class，這樣 CSS 才抓得到
            field.widget.attrs.update({'class': 'form-control'})
            # 2. 如果你覺得 Placeholder 很醜，也可以在這裡統一加
            field.widget.attrs.update({'placeholder': f'請輸入{field.label}'})

        # 修正標籤名稱 (同樣不加冒號)
        self.fields['password1'].label = "密碼"
        self.fields['password2'].label = "密碼確認"
        
        # 提示詞設定
        self.fields['password1'].help_text = "至少 4 個字元，且需含至少一個英文字母"
        self.fields['password2'].help_text = ""