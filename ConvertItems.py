"""Helper Script to Generate Items from CSV
"""
import csv
import json

table = "../TA/table.csv"

with open(table, encoding="UTF-8") as csvfile:
    csv_reader = csv.reader(csvfile)
    line = 0
    for row in csv_reader:
        if line > 1:
            if row[6] == "0":
                ad = "0w0+0"
            else:
                ad = row[6]
            if row[9] == "0":
                ap = "0w0+0"
            else:
                ap = row[9]
            data = {
                "$schema": "../../../.github/workflows/itemschema.json",
                row[0]: {
                    "type": row[2].lower(),
                    "description": row[1],
                    "ad": ad,
                    "ap": ap,
                    "hp": int(row[7]),
                    "ar": int(row[8]),
                    "mr": int(row[10]),
                    "effects": [],
                    "useable": bool(row[11]),
                    "equipable": bool(row[12]),
                    "slots": ["melee"],
                    "questitem": bool(row[14]),
                    "rarity": row[13].lower(),
                },
            }

            json_object = json.dumps(data, indent=4)

            with open(f"../TA/Test/{row[0]}.json", "w", encoding="UTF8") as outfile:
                outfile.write(json_object)
        line += 1

    print(f"Anzahl Datensätze: {line-2}")
