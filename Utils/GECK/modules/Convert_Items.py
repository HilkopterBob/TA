"""Helper Script to Generate Stuff from CSV
"""

import csv
import json
import os
from hashlib import sha256


# GECK Entry-Point
def Convert_Items():
    """GECK entrypoint"""
    CreateContentPack("..\\TA\\Assets\\Core".replace("\\", os.sep))


def cItems():
    """Creates Items from CSV"""
    table = "..\\TA\\table.csv".replace("\\", os.sep)

    with open(table, encoding="UTF-8") as csvfile:
        csv_reader = csv.reader(csvfile)
        line = 0
        for row in csv_reader:
            if line > 1:
                if row[6] == "0":
                    ad = "0w0+0"
                else:
                    ad = row[6]
                if row[10] == "0":
                    ap = "0w0+0"
                else:
                    ap = row[10]
                data = {
                    "$schema": "../../../.github/workflows/itemschema.json",
                    row[0]: {
                        "type": row[2].lower(),
                        "description": row[1],
                        "ad": ad,
                        "ap": ap,
                        "hp": int(row[8]),
                        "ar": int(row[9]),
                        "mr": int(row[11]),
                        "effects": [],
                        "useable": bool(row[12]),
                        "equipable": bool(row[13]),
                        "slots": [x.strip() for x in row[5].lower().split(",")],
                        "blocking": [x.strip() for x in row[6].lower().split(",")],
                        "questitem": bool(row[15]),
                        "rarity": row[14].lower(),
                    },
                }

                json_object = json.dumps(data, indent=4)

                with open(f"../TA/Test/{row[0]}.json", "w", encoding="UTF8") as outfile:
                    outfile.write(json_object)
            line += 1

        print(f"Anzahl Datensätze: {line-2}")


def cEntities():
    """Creates Entities from CSV"""
    table = "../TA/table.csv"

    with open(table, encoding="UTF-8") as csvfile:
        csv_reader = csv.reader(csvfile)
        line = 0
        for row in csv_reader:
            if line > 1:
                print(row[14])
                data = {
                    "$schema": "../../../.github/workflows/entitieschema.json",
                    row[0]: {
                        "name": row[0],
                        "hp": int(row[1]),
                        "wealth": int(row[2]),
                        "inv": [],
                        "xp": int(row[3]),
                        "ptype": [int(x) for x in row[4].split(",")],
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
                            "chr": int(row[12]),
                        },
                        "loottable": row[13],
                        "ai": row[14],
                        "isPlayer": row[15],
                        "Team": row[16],
                    },
                }

                json_object = json.dumps(data, indent=4)

                with open(
                    f"../TA/Core/Entities/{row[0]}.json", "w", encoding="UTF8"
                ) as outfile:
                    outfile.write(json_object)
            line += 1

        print(f"Anzahl Datensätze: {line-2}")


def getChecksum(file):
    """get file checksum"""
    # Calculates SHA256 Checksum for given File
    sha256sum = sha256()
    with open(file, "rb") as f:
        data_chunk = f.read(1024)
        while data_chunk:
            sha256sum.update(data_chunk)
            data_chunk = f.read(1024)

    checksum = sha256sum.hexdigest()

    # Checks if Calculated Checksum is in Checksums File
    return checksum


def CreateContentPack(folder):
    """creates content packs"""

    items = 0
    content = {}
    content["Items"] = {}
    content["Entities"] = {}
    content["Levels"] = {}
    content["Effects"] = {}
    content["Loottables"] = {}
    content["AI"] = {}

    name = str.split(folder, os.sep)[-1]

    # underscore represents dirs
    for subdir, _, files in os.walk(folder):
        for file in files:
            filepath = subdir + os.sep + file

            if filepath.endswith(".json"):
                print(filepath)
                match str.split(filepath, os.sep)[-2]:
                    case "Items":
                        content["Items"][file] = getChecksum(filepath)
                    case "Entities":
                        content["Entities"][file] = getChecksum(filepath)
                    case "Levels":
                        content["Levels"][file] = getChecksum(filepath)
                    case "Effects":
                        content["Effects"][file] = getChecksum(filepath)
                    case "Loottables":
                        content["Loottables"][file] = getChecksum(filepath)
                    case "AI":
                        content["AI"][file] = getChecksum(filepath)
                items += 1

    data = {
        name: {
            "creator": "TheDevs",
            "version": 1.0,
            "description": "The Core Assets of the Game",
            "root": folder,
            "content": content,
        }
    }

    json_object = json.dumps(data, indent=4)

    with open("meta.conf", "w", encoding="UTF8") as f:
        f.write(json_object)


# CreateContentPack("..\\TA\\Assets\\Core")
