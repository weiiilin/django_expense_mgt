from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum # 用於加總金額
from django.utils import timezone
from .models import ExpenseRecord
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .forms import ExpenseForm
from .forms import CustomRegistrationForm # 引入自定義表單

def register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST) # 改用新表單
        if form.is_valid():
            form.save()
            return redirect('expense_mgt:login')
    else:
        form = CustomRegistrationForm()
    return render(request, 'register.html', {'form': form})

def home(request):
    records = ExpenseRecord.objects.all()
    
    # 計算當月總支出
    now = timezone.now()
    current_month_total = ExpenseRecord.objects.filter(
        date__year=now.year, 
        date__month=now.month
    ).aggregate(total=Sum('amount'))['total'] or 0
    
    return render(request, 'home.html', {
        'records': records,
        'current_month_total': current_month_total
    })

# expense_mgt/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.utils import timezone
from .models import ExpenseRecord

@login_required(login_url='expense_mgt:login')
def home(request):
    # --- 1. 初始化與取得參數 ---
    now = timezone.now()
    year = request.GET.get('year')
    month = request.GET.get('month')
    
    # 如果沒傳參數，預設為目前的年、月
    if not year or not month:
        year = now.year
        month = now.month
    else:
        year = int(year)
        month = int(month)

    # --- 2. 資料隔離與過濾 (核心關鍵) ---
    # 先抓出「屬於該使用者」的所有紀錄
    user_records = ExpenseRecord.objects.filter(user=request.user)
    
    # 再從該使用者的紀錄中，過濾出「指定年份與月份」的內容
    # 這樣就保證了 records 裡絕對不會出現別人的帳
    records = user_records.filter(date__year=year, date__month=month)
    
    # --- 3. 計算總支出 ---
    # 同理，這裡的總支出是基於已經過濾過使用者的 records
    current_month_total = records.aggregate(total=Sum('amount'))['total'] or 0
    
    # --- 4. 準備月份選單資料 ---
    # 讓使用者可以切換最近 6 個月的選單邏輯
    month_options = []
    for i in range(6):
        m = (now.month - i - 1) % 12 + 1
        y = now.year + (now.month - i - 1) // 12
        month_options.append({'year': y, 'month': m})

    # --- 5. 渲染頁面 ---
    return render(request, 'home.html', {
        'records': records,
        'current_month_total': current_month_total,
        'selected_year': year,
        'selected_month': month,
        'month_options': month_options,
    })

def delete_expense(request, pk):
    """刪除紀錄後導回首頁"""
    record = get_object_or_404(ExpenseRecord, pk=pk)
    record.delete()
    return redirect('expense_mgt:home')


@csrf_exempt
@login_required
def api_add_expense(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # 將資料餵給 Form
            form = ExpenseForm(data)
            
            if form.is_valid():
                # commit=False 先不存入資料庫，因為我們要手動補上 user
                record = form.save(commit=False)
                record.user = request.user
                record.save()
                return JsonResponse({'status': 'success'})
            else:
                # 如果驗證失敗，回傳具體的錯誤訊息
                errors = form.errors.get_json_data()
                return JsonResponse({'status': 'error', 'message': errors}, status=400)
                
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    # 如果不是 POST 請求，回傳不允許的方法
    return JsonResponse({'status': 'error', 'message': 'Method not allowed'}, status=405)