"""ll_project 的 Django 設定檔。

教學導讀：
1. 先理解「這是全域設定」：會影響整個專案（App、模板、資料庫、登入流程）。
2. 開發環境可先用預設值快速啟動；上線前必須重新檢查安全設定。
3. 本檔最常調整區塊：INSTALLED_APPS、TEMPLATES、DATABASES、AUTH 相關設定。
"""

from pathlib import Path

# 以專案根目錄為基準，後續拼接路徑時可避免硬編碼字串。
BASE_DIR = Path(__file__).resolve().parent.parent


# 開發期快速啟動設定（不適合直接上線）。
# 上線檢查清單：
# https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# 安全提醒：正式環境必須改成環境變數，不要把金鑰明文放在版本控制。
SECRET_KEY = 'django-insecure-mibxt7sboxg%r)9t6z=a6@weyo(thgbknfcwgyowgx9$5s4&=!'

# 安全提醒：DEBUG=True 僅適用開發期，正式環境請務必關閉。
DEBUG = True

ALLOWED_HOSTS = []

# 已啟用的 Django App。
# 載入順序通常不敏感，但中介層（MIDDLEWARE）順序常常很重要。

INSTALLED_APPS = [
    # 專案自訂 app。
    'learning_logs',
    'accounts',

    # 第三方套件 app（例如 Bootstrap 5 模板標籤）。
    'django_bootstrap5',

    # Django 內建功能 app（登入、Session、後台等）。
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'll_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 若要放「專案層級 templates」，可在此加入 BASE_DIR / 'templates'。
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'll_project.wsgi.application'


# 資料庫設定：目前使用 sqlite3，適合教學與小型專案。
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# 密碼強度驗證規則。
# 預設包含：相似度、最短長度、常見密碼、全數字密碼等檢查。

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# 國際化與時區設定。

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# 靜態檔案（CSS / JS / 圖片）URL 前綴。

STATIC_URL = 'static/'

# 未指定主鍵時，模型預設使用 BigAutoField。

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 自訂登入導向設定：
# - 成功登入後導向首頁
# - 登出後導向首頁
# - 若存取需登入頁面，導向 accounts:login
LOGIN_REDIRECT_URL = 'learning_logs:index'
LOGOUT_REDIRECT_URL = 'learning_logs:index'
LOGIN_URL = 'accounts:login'