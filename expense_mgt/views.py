from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum # 用於加總金額
from django.utils import timezone
from .models import ExpenseRecord
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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

def home(request):
    # 1. 取得網頁傳來的年、月參數
    year = request.GET.get('year')
    month = request.GET.get('month')
    
    now = timezone.now()
    
    # 2. 如果沒傳參數，預設為目前的年、月
    if not year or not month:
        year = now.year
        month = now.month
    else:
        year = int(year)
        month = int(month)

    # 3. 過濾該月份的紀錄
    records = ExpenseRecord.objects.filter(date__year=year, date__month=month)
    
    # 4. 計算該月份總支出
    current_month_total = records.aggregate(total=Sum('amount'))['total'] or 0
    
    # 5. 準備月份選單資料（顯示最近 6 個月供切換）
    month_options = []
    for i in range(6):
        # 計算過去每個月的日期
        m = (now.month - i - 1) % 12 + 1
        y = now.year + (now.month - i - 1) // 12
        month_options.append({'year': y, 'month': m})

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
def api_add_expense(request):
    """
    API 視圖：接收前端 fetch 傳來的 POST 請求，將新帳目存入資料庫。
    """
    if request.method == 'POST':
        try:
            # 解析前端傳來的 JSON 內容
            data = json.loads(request.body)
            
            # 從資料中取值並建立新的資料庫紀錄
            # 使用 .get() 可以避免缺少欄位時直接當掉
            record = ExpenseRecord.objects.create(
                date=data.get('date'),  # 前端應該傳來 date 欄位
                category=data.get('category'),
                amount=data.get('amount'),
                description=data.get('description', '')
            )
            
            # 儲存成功後，回傳成功的 JSON 訊息與新資料給前端
            return JsonResponse({'status': 'success'}, status=201)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    # 如果不是 POST 請求，回傳不允許的方法
    return JsonResponse({'status': 'error', 'message': 'Method not allowed'}, status=405)