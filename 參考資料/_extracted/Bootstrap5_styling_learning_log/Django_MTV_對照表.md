# Django MVC/MTV 對照表（learning_logs 專案）

本表整理本專案所有主要頁面（URL）對應的 view、form/model、template，協助你快速理解 Django 的請求處理流程。

| URL 路徑範例                | 對應 view 函式         | 主要 Model/Form         | 對應 template                        | 備註說明 |
|-----------------------------|------------------------|-------------------------|---------------------------------------|----------|
| /                           | index                  | 無                      | learning_logs/index.html              | 首頁，純靜態內容 |
| /topics/                    | topics                 | Topic                   | learning_logs/topics.html             | 主題列表，僅查詢自己的 Topic |
| /topics/<topic_id>/         | topic                  | Topic, Entry            | learning_logs/topic.html              | 單一主題詳情與所有筆記 |
| /new_topic/                 | new_topic              | TopicForm (Topic)       | learning_logs/new_topic.html          | 新增主題表單 |
| /new_entry/<topic_id>/      | new_entry              | EntryForm (Entry)       | learning_logs/new_entry.html          | 新增筆記表單，需指定主題 |
| /edit_entry/<entry_id>/     | edit_entry             | EntryForm (Entry)       | learning_logs/edit_entry.html         | 編輯既有筆記 |
| /accounts/register/         | register (accounts)    | UserCreationForm (User) | registration/register.html            | 使用者註冊 |
| /accounts/login/            | Django 內建 view       | AuthenticationForm      | registration/login.html               | 使用者登入 |
| /accounts/logout/           | Django 內建 view       | 無                      | 無（登出後導向首頁）                   | 使用者登出 |

---

## 流程說明

1. **URL**：使用者在瀏覽器輸入網址，Django 依照 urls.py 決定要呼叫哪個 view。
2. **view**：view 函式負責處理請求（GET/POST），決定要查詢/儲存哪些資料，並選擇要回傳哪個 template。
3. **form/model**：
   - 若有表單輸入，會用 Django Form 處理驗證與資料綁定。
   - 若需存取資料庫，會用 Model 查詢/儲存資料。
4. **template**：view 將資料（context）傳給 template，產生 HTML 回應給使用者。

---

## 進階補充
- Django 其實是 MTV 架構（Model-Template-View），但 view 在 Django 裡負責「控制器」角色。
- 權限檢查、錯誤處理、訊息提示等都在 view 層實作。
- 若有多 app，建議每個 app 都有自己的 urls.py，專案層只負責 include。

---

如需更細節流程圖或想看某頁面的完整 request-response 步驟，請再告知！
