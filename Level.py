"""
Levels Module which holds 2 Classes
    Level()
    Levelinit()
"""

from __future__ import annotations
from typing import TYPE_CHECKING
import json
import random
import os
from Utils import Pr, Logger
from config import entities_folder

# Type Checking Imports
if TYPE_CHECKING:
    from Entities import Entity
    from Items import gitem


class Level:
    """
    Class which defines Levels
    Contains Functions:
    from_json : Creates Levels from JSON
    """

    __slots__ = (
        "name",
        "descr",
        "text",
        "choices",
        "inv",
        "triggers",
        "ltype",
        "entitylist",
        "entityspawn",
    )

    def __init__(
        self,
        text: str = None,
        choices: list[Choice] = None,
        name: str = "Levelnameplatzhalter",
        inv: list[gitem] = None,
        ltype: str = "Testtype",
        descr: (
            str | list[str | dict[str:bool]]
        ) = "Standartdescription du Sohn einer Dirne",
        entitylist: list[Entity] = None,
        entityspawn: list[Entity] = None,
        triggers=list[dict[str:bool]],
    ) -> None:
        if text is None:
            text = []
        if choices is None:
            choices = []
        if inv is None:
            inv = []
        if entitylist is None:
            entitylist = []
        if triggers is None:
            triggers = []
        if entityspawn is None:
            entityspawn = []

        self.name = name
        self.descr = descr
        # self.text = text
        self.choices = self.zip_choices(text, choices)
        self.inv = inv
        self.triggers = triggers
        self.ltype = ltype
        self.entitylist = entitylist
        self.entityspawn = entityspawn

        self.onLevelCreate()
        self.populate()

    def __str__(self) -> str:
        return f"{self.name}"

    # Commented out for readability in Logfile - need to find a workaround
    # def __repr__(self):
    #    return f"[{self.__class__.__module__}.{self.__class__.__name__}([{self.text}],[{self.choices}],'{self.name}',[{self.inv}],'{self.ltype}','{self.descr}',[{self.entitylist}],[{self.entityspawn}],[{self.triggers}]) at <{hex(id(self))}>]"  # pylint:disable=C0301

    @staticmethod
    def from_json(json_dct: dict, lname: str) -> Level:
        """Creates a Level from JSON

        Args:
            json_dct (JSON): Json Data to be parsed
            lname (String): Levelname

        Returns:
            Level: Level
        """
        return Level(
            json_dct["text"],
            json_dct["choices"],
            lname,
            json_dct["inv"],
            json_dct["ltype"],
            json_dct["descr"],
            json_dct["entitylist"],
            json_dct["entityspawn"],
            json_dct["triggers"],
        )

    def change_entity_list(
        self, ctype: str, entity: Entity
    ) -> bool:  # TODO: Change Ctype to Integer or Bool
        """
        Changes the list of entities for specific level

        :ctype: + for adding, - for subtracting entity from list

        :entity: the entity obj

        :dbg: debug, default = True

        =return= returns True if seccessfull, else false
        """
        match ctype:
            case "+":
                Logger.log(
                    f"Entitylist of Level {self}: {[str(x) for x in self.entitylist]}"
                )
                Logger.log(f"Trying to add {entity} to {self}")
                try:
                    for e in self.entitylist:
                        if e.name == entity.name:
                            raise Exception(
                                f"{entity} \
                                            is already in entitielist of Level \
                                            {self} \
                                            and thus cannot be added."
                            )
                    self.entitylist.append(entity)
                    self.onEntityJoin(entity)
                    Logger.log(f"{entity} got added to Level {self}")
                    Logger.log(
                        f"Entitylist of Level {self}: {[str(x) for x in self.entitylist]}"
                    )
                    Logger.log(
                        f"Changing Entity Location Var from Level for Entity: {entity}",
                        2,
                    )
                    entity.location = self
                    return True
                except Exception as e:
                    Logger.log(e, 4)
                    return False
            case "-":
                Logger.log(
                    f"Entitylist of Level {self}: {[str(x) for x in self.entitylist]}"
                )
                Logger.log(f"Trying to remove {entity.name} from {self}")
                try:
                    self.entitylist = list(
                        filter(lambda e: e.name != entity.name, self.entitylist)
                    )
                    self.onEntityLeave(entity)
                    Logger.log(f"{entity.name} got removed from Level {self}")
                    Logger.log(
                        f"Entitylist of Level {self}: {[str(x) for x in self.entitylist]}"
                    )
                    return True
                except:
                    return False
            case _:
                return Logger.log("got no right ctype. choose between + and -", 1)

    def printDesc(self) -> None:
        """Prints Level Description to User"""
        for entry in self.descr:
            if len(entry) > 1:
                if isinstance(entry, str):
                    Pr.n(f"{str(entry)}")
                    continue
                if entry[1] in self.triggers:
                    Pr.n(f"{str(entry[0])}")
                continue

    def getAvailableChoices(self) -> list[Choice]:
        """Returns the Choices currently available to the User

        Returns:
            list: Choices
        """
        achoices = []
        for choice in self.choices:
            # The following part adds choices without trigger
            #     to the availibleChoices.
            #     Choices with trigger get added if
            #     Level.triggers[n] == Choice.allow_trigger

            if choice.allow_trigger is None:
                achoices.append(choice)
            elif isinstance(choice.allow_trigger, dict):
                for set_trigger in self.triggers:
                    if set_trigger == choice.allow_trigger:
                        achoices.append(choice)
            else:
                Logger.log(
                    f"Unsupported allow_trigger in Choice! {choice.allow_trigger}"
                )

        return achoices

    def printChoices(self) -> bool:
        """Prints the Available Choices to the User

        Returns:
            Boolean: True
        """
        i = 1
        for llist in self.choices:
            if len(llist) == 1 and llist[0] != "":
                Pr.n(f"{i}. {llist[0]}")
                i = i + 1
            elif len(llist) > 1:
                for ddict in self.triggers:
                    if llist[1] == ddict:
                        Pr.n(f"{i}. {llist[0]}")
                        i = i + 1
        return True

    def levelname(lobject: Level) -> str | None:
        """Return the Name of an Levelobject

        Args:
            object (Level): Level from what you wan't the Objectname

        Returns:
            String: Levelname
        """
        try:
            return lobject.name
        except Exception as e:
            Logger.log(f"ERR: {e}", 2)
            return None

    def populate(self) -> int | None:  # pylint: disable=R1710
        """Populates the Level with Entities from Spawnlist

        Returns:
            Array: List of Entities
        """
        from Entities import EntityInit  # pylint: disable=C0415

        _entitiestospawn = self.entityspawn

        if _entitiestospawn is None or len(_entitiestospawn) < 1:
            Logger.log("No Entities to Spawn in this Level", 2)
            return 1

        _amount = random.randrange(1, len(_entitiestospawn))
        Logger.log(f"Entities to spawn: {_entitiestospawn}, Amount: {_amount}")

        _dict = list(_entitiestospawn.keys())
        _weights = list(_entitiestospawn.values())

        Logger.log(f"Trying to Spawn {_amount} Entities", 1)
        _entity = random.choices(_dict, weights=_weights, k=_amount)
        _entityreturn = []

        for i in _entity:
            Logger.log(f"Loading Entity {i} from Assets", 0)
            _entityreturn.append(
                EntityInit.load_entities_by_name_from_json(
                    f"{entities_folder}{os.sep}{i}.json", i
                )
            )

        for e in _entityreturn:
            Logger.log(f"Adding spawned Entity {e} to Level", 1)
            self.change_entity_list("+", e)
        return

    def onLevelCreate(self) -> None:
        """This is called whenever an Level is created"""
        Logger.log(f"Created Instance of Level: {self}", 0)

    def onEntityJoin(self, entity: Entity) -> None:
        """This is called whenever an Entity joins a Level

        Args:
            entity (entity): Entity which is joining the Level
        """
        Logger.log(f"Entity:{entity} joined Level: {self}", 0)
        if entity.isPlayer:
            if len(self.entitylist) > 1:
                # TODO: Add Chance to put Player into Combat
                # TODO: Change Chance based on Entity hostility
                Logger.log(f"Entitylist of Level: {self.entitylist}", -1)

                Pr.n(f"Du wirst von {self.entitylist[0]} angegriffen!")

                entity.actionstack.insert(  # pylint: disable=E1101
                    0, ["change_gamestate", ["combat"]]
                )

    def onEntityLeave(self, entity: Entity) -> None:
        """This is called whenever an Entity Leaves a Level

        Args:
            entity (entity): Entity which is leaving the Level
        """
        Logger.log(f"Entity:{entity} left Level: {self}", 0)

    def zip_choices(self, text: list[str | dict], choices: list[Choice]) -> dict:
        """This is called whenever a level gets created and populates
        its choices.

        Args:
            text (list[string, {action}]): Follow-up text and actions
            choices (list): all hardcoded choices
        """

        zipped_choices = []

        for index, choice in enumerate(choices):
            zipped_choices.append(
                Choice(text[index], choice, choice[1] if len(choice) > 1 else None)
            )

        return zipped_choices


class LevelInit:
    """
    Class which Initializes Levels
    Contains Functions:
    load_all_levels_from_json : Loads all available Levels from a Json File
    load_level_by_name_from_json : Loads an Level by it's Name from a Json File

    """

    def load_all_levels_from_json(
        json_file, _curLevels: list[Level] = None
    ) -> list[Level]:
        """
        Return alls Levels from Json file

        :json_file (File): Json file to load Levels from
        :_curLevels (List): Internally used for recursion

        =return= List of all Levels loaded from Json
        """
        if _curLevels is None:
            _curLevels = []
        curLevels = _curLevels

        Logger.log(f"Loading Levels from: {json_file}")

        data = {}

        if json_file:
            if not isinstance(json_file, dict):
                with open(json_file, encoding="UTF-8") as json_data:
                    data = json.load(json_data)
            else:
                data = json_file

        for lname in data.keys():
            if lname[0] != "$":
                if data[lname].get("child_levels"):
                    childlevels = data[lname].get("child_levels")
                    LevelInit.load_all_levels_from_json(childlevels, curLevels)
                curLevels.append(Level.from_json(data[lname], lname))
        return curLevels

    def load_level_by_name_from_json(json_file, name: str) -> Level:
        """
        Return a single Level Object from Json/File by given Name

        :json_file (File): Json File to load Level from

        =return= Level object
        """
        if json_file:
            if not isinstance(json_file, dict):
                with open(json_file, encoding="UTF-8") as json_data:
                    data = json.load(json_data)
            else:
                data = json_file

            for lname in data.keys():
                if name == lname:
                    return Level.from_json(data[lname], lname)
            Logger.log(f"Levelname: {name} not found!", 1)
        return False


class Choice:
    """
    Class witch defines Choices.
    """

    def __init__(
        self,
        text: list[str | dict[str:bool]],
        choice: list[str | dict[str:bool]],
        allow_trigger: dict[str:bool] = None,
    ) -> None:
        self.choice = choice
        self.text = text
        self.allow_trigger = allow_trigger
