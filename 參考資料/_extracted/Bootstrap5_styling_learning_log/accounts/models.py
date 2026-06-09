from django.db import models

# 目前 accounts app 尚未擴充自訂模型。
# 若未來需要額外使用者欄位，可考慮：
# 1. 建立 Profile（OneToOne 對應 User）
# 2. 或改用自訂 User model（需在專案早期決定）
