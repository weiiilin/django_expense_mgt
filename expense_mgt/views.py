from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import CustomRegistrationForm
from .models import ExpenseRecord


def _build_month_options(now):
    month_options = []
    for i in range(6):
        month_index = now.month - i - 1
        month_options.append({
            'year': now.year + month_index // 12,
            'month': month_index % 12 + 1,
        })
    return month_options


def register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_mgt:login')
    else:
        form = CustomRegistrationForm()
    return render(request, 'register.html', {'form': form})


@login_required(login_url='expense_mgt:login')
def home(request):
    now = timezone.now()
    period = request.GET.get('period')
    if period and '-' in period:
        year_str, month_str = period.split('-', 1)
        year = int(year_str)
        month = int(month_str)
    else:
        year = now.year
        month = now.month

    records = ExpenseRecord.objects.filter(user=request.user, date__year=year, date__month=month)
    current_month_total = records.aggregate(total=Sum('amount'))['total'] or 0

    return render(request, 'home.html', {
        'records': records,
        'current_month_total': current_month_total,
        'selected_year': year,
        'selected_month': month,
        'month_options': _build_month_options(now),
    })


@login_required(login_url='expense_mgt:login')
def expense_edit(request, pk):
    record = get_object_or_404(ExpenseRecord, pk=pk, user=request.user)
    return render(request, 'expense_edit.html', {'record': record})