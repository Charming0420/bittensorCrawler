import os
import pandas as pd

folder = "BinanceCSVData"

output_filename = "merged_taoToBinance.csv"

csv_files = [os.path.join(folder, f"taoToBinance{i}.csv") for i in range(1, 254)]

combined_csv = pd.DataFrame()

for i, file in enumerate(csv_files):
    df = pd.read_csv(file)
    if i == 0:
        combined_csv = df
    else:
        combined_csv = pd.concat([combined_csv, df], ignore_index=True)

combined_csv.to_csv(output_filename, index=False)

print(f"所有 CSV 檔案已合併到 {output_filename}")