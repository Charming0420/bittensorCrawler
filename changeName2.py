import os
import shutil
import re

# 原資料夾和新資料夾的路徑
original_folder = "CSVData"
new_folder = "BinanceCSVData"

# 創建新資料夾
os.makedirs(new_folder, exist_ok=True)

# 定義正則表達式來匹配檔案名中的時間戳
pattern = re.compile(r'transfer-5GBnPzvPghS8AuCoo6bfnK7JUFHuyUhWSFD4woBNsKnPiEUi - 2024-07-10T(\d+)\.\d+\.csv')

# 找出所有符合模式的檔案並排序
files = []
for filename in os.listdir(original_folder):
    match = pattern.match(filename)
    if match:
        timestamp = int(match.group(1))
        files.append((timestamp, filename))

# 按照時間戳排序
files.sort()

# 複製並重命名檔案
for index, (timestamp, filename) in enumerate(files, start=101):
    original_filename = os.path.join(original_folder, filename)
    new_filename = os.path.join(new_folder, f"taoToBinance{index}.csv")
    if os.path.exists(original_filename):
        shutil.copy2(original_filename, new_filename)
        print(f"複製並重命名: {original_filename} -> {new_filename}")
    else:
        print(f"檔案未找到: {original_filename}")

print("檔案複製和重命名完成")