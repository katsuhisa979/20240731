# ソースコード
import openpyxl
import os
from datetime import datetime

wb = openpyxl.Workbook()
current_date = datetime.now()

# この1行を追記(請求書_2024年07月)
output_folder = f"請求書_{current_date.strftime('%Y年%m月')}"
print(output_folder)
# フォルダを作成
os.makedirs(output_folder, exist_ok=True) #（編集済み） 

#リアクションする

#返信








