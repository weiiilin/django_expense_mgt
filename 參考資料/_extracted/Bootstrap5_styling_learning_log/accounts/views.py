from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """註冊新使用者。

    GET: 顯示註冊表單
    POST: 驗證資料、建立帳號、直接登入
    """
    if request.method != 'POST':
        # 初次進入頁面，顯示空白表單。
        form = UserCreationForm()
    else:
        # 將使用者提交資料綁定到 Django 內建註冊表單。
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            # 儲存新使用者（會建立 User 紀錄）。
            new_user = form.save()
            # 註冊成功後自動登入，減少再次輸入帳密的摩擦。
            login(request, new_user)
            return redirect('learning_logs:index')

    # 驗證失敗時，form 內含錯誤訊息，模板可直接顯示。
    context = {'form': form}
    return render(request, 'registration/register.html', context)