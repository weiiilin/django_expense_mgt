 # Django Expense MGT

這個專案參考了附件中的 Bootstrap 5 與雲端部署教材，完成以下目標：

- 使用 Bootstrap 5 美化登入、註冊與記帳首頁
- 導入 Django REST Framework，提供至少兩個 REST API
- 改用 MySQL，並可透過 Docker Compose 一鍵啟動
- 提供可在瀏覽器操作的網頁介面，並可用 Postman 測試 API

## 功能

- 使用者註冊、登入、登出
- 新增、查詢、編輯、刪除消費紀錄
- 依月份切換歷史紀錄
- REST API
	- `GET /api/expenses/`
	- `POST /api/expenses/`
	- `GET /api/expenses/<id>/`
	- `PATCH /api/expenses/<id>/`
	- `DELETE /api/expenses/<id>/`

## 本機開發

1. 建立虛擬環境並安裝套件

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

2. 執行資料庫遷移與啟動網站

```bash
python manage.py migrate
python manage.py runserver
```

3. 開啟瀏覽器

```text
http://127.0.0.1:8000/
```

## Docker Compose 部署

以下流程模擬雲端部署環境，使用 MySQL 官方映像與 Django Web 容器。

1. 在 GitHub 建立帳號，並建立與專案同名的空白 Repository。

2. 將本地專案推上 GitHub。

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <你的 GitHub Repository URL>
git push -u origin main
```

3. 將 GitHub 專案 clone 到你的模擬環境。

```bash
git clone <你的 GitHub Repository URL>
cd django_expense_mgt
```

4. 使用 Docker Compose 啟動多容器專案。

```bash
docker compose up --build
```

5. 開啟瀏覽器並進入網站。

```text
http://127.0.0.1:8000/
```

6. 使用 Postman 測試 API。

```text
GET    /api/expenses/
POST   /api/expenses/
GET    /api/expenses/<id>/
PATCH  /api/expenses/<id>/
DELETE /api/expenses/<id>/
```

## Docker Compose 服務

- `db`：MySQL 8.0 官方映像
- `web`：Django + DRF Web 服務，使用 Gunicorn 啟動

## 注意事項

- API 採用登入後的 Session 驗證，也同時保留 Basic Auth，方便 Postman 測試。
- 預設 Docker Compose 已內建 MySQL 連線環境變數。
- 若要建立後台管理員，可以在容器中執行 `python manage.py createsuperuser`。


