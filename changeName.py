import os
import shutil

original_folder = "CSVData"
new_folder = "BinanceCSVData"

os.makedirs(new_folder, exist_ok=True)

for i in range(1, 101):
    original_filename = os.path.join(original_folder, f"transfer-5GBnPzvPghS8AuCoo6bfnK7JUFHuyUhWSFD4woBNsKnPiEUi ({i}).csv")
    new_filename = os.path.join(new_folder, f"taoToBinance{i}.csv")
    if os.path.exists(original_filename):
        shutil.copy2(original_filename, new_filename)
        print(f"複製並重命名: {original_filename} -> {new_filename}")
    else:
        print(f"檔案未找到: {original_filename}")

print("檔案複製和重命名完成")