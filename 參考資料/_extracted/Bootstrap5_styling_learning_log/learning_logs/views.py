from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """Learning Log 首頁。

    此頁通常作為導覽入口，不需查詢資料庫也可先顯示。
    """
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """顯示目前登入使用者的所有主題。"""
    # 只查自己的資料，避免看到其他使用者內容。
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """顯示單一主題與其底下所有筆記。"""
    # 依 URL 參數抓出主題。
    topic = Topic.objects.get(id=topic_id)
    # 權限檢查：不是自己的資料就回 404，避免洩漏資源存在與否。
    if topic.owner != request.user:
        raise Http404

    # 以時間新到舊排序，最新筆記先看到。
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """新增主題。

    GET: 顯示空白表單
    POST: 驗證後儲存資料
    """
    if request.method != 'POST':
        # 第一次進入頁面時，建立空白表單。
        form = TopicForm()
    else:
        # 使用者送出資料後，將 POST 內容綁定到表單。
        form = TopicForm(data=request.POST)
        if form.is_valid():
            # commit=False 讓我們先拿到物件，再補上 owner 後儲存。
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    # 驗證失敗時，form 會帶著錯誤訊息回傳給模板顯示。
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """在指定主題下新增一則筆記。"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # 第一次進入頁面，顯示空白表單。
        form = EntryForm()
    else:
        # 提交後進行驗證。
        form = EntryForm(data=request.POST)
        if form.is_valid():
            # 先建立但不存，補上外鍵 topic 後再儲存。
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # 回傳表單（可能是空白，也可能含錯誤訊息）。
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """編輯既有筆記。"""
    # 先抓筆記，再取得其所屬 topic。
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    # 僅允許筆記擁有者編輯。
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # 初次載入：使用 instance 預填原始內容。
        form = EntryForm(instance=entry)
    else:
        # 送出後：同時帶入 instance + data，代表「更新」而不是「新增」。
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)