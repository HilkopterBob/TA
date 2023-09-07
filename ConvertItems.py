import csv
import json
from Items import itemInit, gitem


table = "../TA/table.csv"
with open(table) as csvfile:
    csv_reader = csv.reader(csvfile)
    zeilennummer = 0
    for row in csv_reader:
        if zeilennummer > 1:
            b = "false"
            data = {
                "$schema": "../../../.github/workflows/itemschema.json",
                row[0]: {
                    "type": row[3],
                    "description": row[1],
                    "ad": row[6],
                    "ap": row[9],
                    "hp": row[7],
                    "ar": row[8],
                    "mr": row[10],
                    "effects": [],
                    "useable": row[13],
                    "equipable": row[11],
                    "slots": ["melee"],
                    "questitem": b,
                    "rarity": row[12],
                },
            }

            json_object = json.dumps(data, indent=4)

            with open(f"../TA/Test/{row[0]}.json", "w") as outfile:
                outfile.write(json_object)
        zeilennummer += 1

    print(f"Anzahl Datensätze: {zeilennummer-2}")
