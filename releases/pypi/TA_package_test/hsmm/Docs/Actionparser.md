# Actionparser

---

### Beschreibung

Der Actionparser wird genutzt um Vodefinierte Funktionen via String und Übergeben Parametern auszuführen um so auf Actions aus dem Actionstack zu reagieren
Ein Beispiel um auf dem Spieler (Player) den Effekt (Kopfschmerz) anzuwenden (applyeffect)

`actionparser.callfunction(["applyeffect",["Player","Kopfschmerz"]]))`

Diese Methode ruft im Actionparser die Funktion "applyeffect" mit den Parametern: [Player,"Kopfschmerz"] auf


### Callstack:

>1. actionparser
>2. callfunction
>3. actionparser
>4. applyeffect
>5. config
>6. effects_file
>7. EffectInit
>8. load_effect_by_name_from_json
>9. return


## I/O

### Expected Inputs: <callfunction(attr=[])>
    attr = ["",["","",""]]
    #<Array>    Multidimensional Array Consisting of attr[0] and attr[1]
    #<String>   attr[0] String of Functionname which should be executed
    #<Array>    attr[1] Array of Parameters for Functionname which should be executed

### Expected Outputs: None
    returns 0 if executed otherwise breaks



# Current Functions

- applyeffect
- takeeffects

### Applyeffect

TODO:
[ ] Actually apply Effect and not only write it to DBG

Die Funktion ist zum Anwenden eines Effektes auf eine Entität

Aus dem Vorherigen Beispiel wäre der Funktionsaufruf wie folgt:

`applyeffect([Player, "Kopfschmerz"])`

### I/O

#### Expected Inputs: <applyeffect(attributes=[])>
    attributes = ["",""]
    #<Object>   attributes[0]   Die Entität die den Effekt bekommen soll
    #<String>   attributes[1]   String des Effektnamen der aus der Effects_JSON gelesen, erstellt und dann angewandt wird

#### Expected Outputs: None
    returns 0 if executed otherwise breaks


### Takeffects

Die Funktion ist zum ausführen des Effektes auf einer Entität

`takeeffects([Player, Kopfschmerz])`

### I/O

#### Expected Inputs: <takeeffects(attributes=[])>
    attributes = ["",""]
    #<Object>   attributes[0]   Die Entität auf die der Effekt angewendet werden soll
    #<Object>   attributes[1]   Das Effekt Objekt welches auf die Entität angewendet werden soll

#### Expected Outputs: None
    returns 0 if executed otherwise breaks
