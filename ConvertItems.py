"""Helper Script to Generate Stuff from CSV
"""
import csv
import json


def cItems():
    """Creates Items from CSV
    """
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
                        "slots": [x.strip() for x in row[5].lower().split(",")],
                        "questitem": bool(row[14]),
                        "rarity": row[13].lower(),
                    },
                }

                json_object = json.dumps(data, indent=4)

                with open(f"../TA/Test/{row[0]}.json", "w", encoding="UTF8") as outfile:
                    outfile.write(json_object)
            line += 1

        print(f"Anzahl Datensätze: {line-2}")

def cEntities():
    """Creates Entities from CSV
    """
    table = "../TA/table.csv"

    with open(table, encoding="UTF-8") as csvfile:
        csv_reader = csv.reader(csvfile)
        line = 0
        for row in csv_reader:
            if line > 1:
                data = {
                    "$schema": "../../../.github/workflows/entitieschema.json",
                    row[0]: {
                        "name": row[0],
                        "hp": int(row[1]),
                        "wealth": int(row[2]),
                        "inv": [],
                        "xp": int(row[3]),
                        "ptype": int(row[4]),
                        "geffects": [],
                        "beffects": [],
                        "eeffects": [],
                        "location": "",
                        "level": int(row[5]),
                        "allowdamage": bool(row[6]),
                        "slots": [],
                        "attributes": {
                        "str": int(row[8]),
                        "dex": int(row[9]),
                        "int": int(row[10]),
                        "ini": int(row[11]),
                        "chr": int(row[12])
                        }
                    },
                }

                json_object = json.dumps(data, indent=4)

                with open(f"../TA/Test/{row[0]}.json", "w", encoding="UTF8") as outfile:
                    outfile.write(json_object)
            line += 1

        print(f"Anzahl Datensätze: {line-2}")


cEntities()
