import csv
import json

# https://www.aozora.gr.jp/index_pages/person_all.html
# CSVファイルの読み込み
csv_file = 'list_person_all_utf8.csv'
json_file = 'aikoku_bunko.json'

# CSVファイルを開いて、JSON形式に変換
with open(csv_file, encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    data = []

    # ヘッダーをスキップする
    next(reader)

    for row in reader:
        data.append({
            "author": row[1],  # 2カラム目
            "title": row[3],   # 4カラム目
            "title_id": row[2] # 3カラム目
        })
# JSONファイルに書き出し
with open(json_file, 'w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, ensure_ascii=False, indent=2)

print(f"{csv_file} has been converted to {json_file}")