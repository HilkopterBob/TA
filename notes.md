# Notes

- [Notes](#notes)
  - [Gameloop](#gameloop)
      - [Effects:](#effects)
      - [Spawn:](#spawn)
  - [Ideen](#ideen)
  - [Stat-/Levelsystem](#stat-levelsystem)



## Gameloop

#### Effects:
    -   evil effects  player → player      *(Bosseffekte, schwere vergiftung, flüche)*
    -   good effects  player → player      *(Healing, speed)*
    -   bad effects   player → player      *(Poisoning)*
    -   good effects  player → level       *("Beleuchtung" → verringert def Demonen)*
    -   bad effects   player → level       *("Lockmittel" → erhöht Chance auf Enemy encounter)*
</br>

#### Spawn:
    -   Spawn chance:
        -   Level spawn chance  *(eg. 10%)*
        -   Level effects       *(eg. "Lockmittel" → + 15%)*
        -   Player effects      *(eg. "Laut" → + 7,5%)*
        -   10% + 15% + 7,5% = 32,5% spawn chance
    -   Spawn:
        -   Level versucht gegner in freien slots zu spawnen
            -   Falls erfolgreich: Platzieren im level
            -   Falls gescheitert: nächster freier Slot im Level
            -   wdh. bis alle Slots bearbeitet
</br>

## Ideen

- Statsystm:
  - Strength
  - Agility
  - etc


## Stat-/Levelsystem
guckt discord
