"""module for G.E.C.K.
creates json files for items from csv
"""

# pylint: disable=unspecified-encoding
# pylint: disable=line-too-long

import csv
import json
import os


def replace_umlauts(string):
    """replaces non-ascii chars"""
    umlaut_map = {
        "ä": "ae",
        "ö": "oe",
        "ü": "ue",
        "Ä": "Ae",
        "Ö": "Oe",
        "Ü": "Ue",
        "ß": "ss",
    }
    for umlaut, replacement in umlaut_map.items():
        string = string.replace(umlaut, replacement)
    return string


def items_csv_to_jsons():
    """creates json file for row in csv

    Args:
        csv_file (str): path to csv
    """
    csv_file = input("Bitte geben Sie den Pfad zur CSV-Datei an: ")
    delimiter = (
        input(
            "Bitte geben Sie das Trennzeichen der"
            "CSV-Datei an (Standardmäßig ein Komma): "
        )
        or ","
    )
    json_folder = "generated_items"
    os.makedirs(json_folder, exist_ok=True)
    json_folder = "generated_items"
    os.makedirs(
        json_folder, exist_ok=True
    )  # Unterordner erstellen, falls er nicht existiert

    with open(csv_file, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=delimiter)
        for row in reader:

            ap = row.get("AP", "")
            ad = row.get("AD", "")

            # Wert für AP und AD anpassen, falls 0 in der CSV
            if ap == "0":
                ap = "0w0+0"
            if ad == "0":
                ad = "0w0+0"

            json_data = {
                "name": replace_umlauts(row.get("Name", "")),
                "type": replace_umlauts(row.get("Category", "")),
                "desc": replace_umlauts(row.get("Description", "")),
                "ad": ad,
                "ap": ap,
                "hp": int(row.get("HP", 0)),
                "ar": int(row.get("AR", 0)),
                "mr": int(row.get("MR", 0)),
                "useable": bool(row.get("Useable", False)),
                "equipable": bool(row.get("Equipable", False)),
                "slots": row.get("Slot", "").split(","),
                "questitem": bool(row.get("QuestItem", False)),
                "rarity": replace_umlauts(row.get("BaseRarity", "common")),
                "effects": row.get("Effects", "").split(","),
            }

            # JSON-Datei schreiben
            json_file = f"{replace_umlauts(row['Name'])}.json"
            json_path = os.path.join(json_folder, json_file)
            with open(json_path, "w", encoding="utf-8") as json_file:
                json.dump(
                    {
                        "$schema": "../../.github/workflows/itemschema.json",
                        replace_umlauts(row["Name"]): json_data,
                    },
                    json_file,
                    indent=4,
                    ensure_ascii=True,
                )

    print(
        f"Konvertierung abgeschlossen! Die JSON-Dateien wurden im Ordner '{json_folder}' erstellt."
    )
