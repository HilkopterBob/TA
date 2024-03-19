# Assethandler Documentation

## Beschreibung

Der Assethandler wird genutzt um jegliche Game Assets zu Initialisieren und Bereitzustellen

## TOC

- [Klassen](#klassen)
- [Attribute](#attribute)

## Klassen

### - `AssetHandler`

Die Basisklasse des Assethandlers

#### Variablen

`allLevels`
`allEntities`
`allItems`
`allEffects`
`Assetpacks`

#### Methoden

`getFiles`
`importLevels`
`importEntities`
`importItems`
`importEffects`

### - `Assetpack`

Die Basisklasse der Assetpacks

#### Attribute

Attribute werden aus dem jeweiligen Assetpack aus der `meta.conf` Datei geladen. Folgende Attribute stehen dann zur Verfügung

- `name` -> STR : Der Name des Assetpacks
- `creator` -> STR : Der Ersteller des Assetpacks
- `version` -> INT : Die Aktuelle Version des Assetpacks
- `description` -> STR : Die Beschreibung des Assetpacks
- `root` -> PATH : Der Basispfad des Assetpacks
- `content` -> DICT : Enthält Alle Levels, Entities, Items, Effect, Loottables und AiTables  
- `levels` -> DICT : Enthält alle Leveldateien & Dateihashes im Format `'Levelname' : 'Dateihash'`
- `entities` -> DICT : Enthält alle Entitiedateien & Dateihashes im Format `'Entityname' : 'Dateihash'`
- `items` -> DICT : Enthält alle Itemdateien & Dateihashes im Format `'Itemname' : 'Dateihash'`
- `effects` -> DICT : Enthält alle Effectdateien & Dateihashes im Format `'Effectname' : 'Dateihash'`
- `loottables` -> DICT : Enthält alle Loottabledateien & Dateihashes im Format `'Loottablename' : 'Dateihash'`
- `ai` -> DICT : Enthält alle AITabledateien & Dateihashes im Format `'AITablename' : 'Dateihash'`
- `unknown` -> DICT : Enthält alle Unbekannten Dateien & Dateihashes im Format `'Dateiname' : 'Dateihash'`
- `valid` -> Bool : Ist das Assetpack Validiert wurden oder nicht

#### Methoden

`validate` : Methode zum abgleichen der aktuellen Dateihashes mit den im Assetpack definierten Dateihashes; Returns: True / False
