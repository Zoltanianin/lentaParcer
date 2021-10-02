import requests
import json
import csv
import headers
import time

url = "https://lenta.com/api/v1/skus/list"

resp_krasota_i_zdorove = requests.post(url, headers=headers.headers_krasota_i_zdorove, data=headers.
                                       data_headers_krasota_i_zdorove).json()
resp_podgus = requests.post(url, headers=headers.headers_podgus, data=headers.data_podgus).json()
date_string = time.strftime("%d%m%Y")
with open('./in/красота_и_здоровье_' + date_string + '.json', 'w', encoding='utf-8') as f:
    json.dump(resp_krasota_i_zdorove, f, ensure_ascii=False, indent=4)
f.close()
with open('./in/подгузники_' + date_string + '.json', 'w', encoding='utf-8') as f:
    json.dump(resp_podgus, f, ensure_ascii=False, indent=4)
f.close()
with open('./in/красота_и_здоровье_' + date_string + '.json', mode='r', encoding='utf-8') as f:
    data = json.load(f)
    skus = data["skus"]
f.close()
with open('./out/каталог_' + date_string + '.xlsx', 'w') as f:
    fieldnames = skus[0]
    writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator='\n')
    writer.writeheader()
    for sku in skus:
        writer.writerow(sku)
f.close()
with open('./in/подгузники_' + date_string + '.json', mode='r', encoding='utf-8') as f:
    data = json.load(f)
    skus = data["skus"]
f.close()
with open('./out/каталог_' + date_string + '.xlsx', 'a') as f:
    fieldnames = skus[0]
    writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator='\n')
    for sku in skus:
        writer.writerow(sku)
f.close()
print("Готово")