# Effekte 

---

### Beschreibung 

Die Effekt Klasse wird genutzt um Effekte zu definieren die Entitäten beeinflussen.
Objekte können mit

`Effect.from_json(data[json_data], effectname)`

Initialisiert werden. Und stehen dann als solche während der Laufzeit zur verfügung.

## Effectinit

Diese Klasse stellt Methoden zur verfügung um Effekte zu Initialisieren

- `load_all_effects_from_json(json_file)`
- `load_effect_by_name_from_json(json_file, name)`

## load_all_effects_from_json(json_file)

Lädt alle vorhanden Effekte aus der gegeben JSON Datei aus und gibt eine Liste mit Effektobjekten zurück

## I/O

### Expected Inputs:
    json_file <FILE>    Json Datei welche alle Objekte beinhaltet

### Expected Outputs: 
    List <Array>        Liste mit Effekt Objekten


## load_effect_by_name_from_json(json_file, name)

Lädt den benannten Effekt aus der gegeben JSON Datei

## I/O

### Expected Inputs:
    json_file <FILE>    Json Datei welche das Objekt beinhaltet
    name      <STRING>  Name des Effektes der gesucht wird

### Expected Outputs: 
    Object <Effect>        Das Effekt Objekt welches erstellt wurde