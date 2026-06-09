from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    """主題建立/編輯表單。

    ModelForm 會依模型欄位自動產生表單元件，
    可大幅減少重複撰寫欄位驗證程式。
    """

    class Meta:
        # 指定這個表單對應的模型。
        model = Topic
        # 僅開放 text 欄位給使用者輸入。
        fields = ['text']
        # 空字串代表不顯示欄位標籤（可改為自訂文案）。
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    """筆記建立/編輯表單。"""

    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        # 調整 textarea 寬度，讓輸入長文更舒適。
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}