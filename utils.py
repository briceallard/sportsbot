import csv
import json


def csv_to_json(csvFilePath, jsonFilePath):
    data = {}

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
            key = rows['game_id']
            data[key] = rows

        with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
            jsonf.write(json.dumps(data, indent=4))


def year_plus_one(year):
    year = int(year)
    year += 1
    return str(year)
