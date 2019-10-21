import json
import datetime
import csv

date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d").split("-")
# today_day = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%d")

# Path for our json file
path = r"PATH"

with open(path, 'r') as f:
    data_json = json.loads(f.read())

with open(f"Pepper {'.'.join(date[::-1])}.csv", 'w', newline='\n', encoding='utf_8_sig') as csvfile:
    fieldnames = ['hot', 'text', 'promo_cost', 'normal_cost', 'url', 'date']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()
    for data in data_json:
        writer.writerow({'hot':         str(data['hot']).replace("\n", "").replace(";", ":"),
                         'text':        str(data['text']).replace("\n", "").replace(";", ":").replace("-", ""),
                         'promo_cost':  str(data["promo_cost"]).replace("\n", "").replace(";", ":"),
                         'normal_cost': str(data["normal_cost"]).replace("\n", "").replace(";", ":"),
                         'url':         str(data["url"]).replace("\n", "").replace(";", ":"),
                         'date':        str(data["date"]).replace("\n", "").replace(";", ":")
                         })
