"""Assethandler for importing needed Assets
"""

import os
import json
import sys

from hashlib import sha256
from time import process_time
from tqdm import tqdm
from Level import LevelInit
from Entities import EntityInit
from Effect import EffectInit
from Items import itemInit
from Utils import Logger
from config import dbg


class AssetHandler:
    """Handles import of Assets from Assets Folder

    Returns:
        None: None
    """

    allLevels = []
    allEntities = []
    allEffects = []
    allItems = []
    Assetpacks = []

    def getFiles(folder: str) -> list:
        """Gets all Json Files from a Folder

        Args:
            folder (Path): Path to Folder to look for Files

        Returns:
            List: List of Paths to Files
        """
        Logger.log(f"Gathering Assets from: {folder}", 1)
        _folder_name = folder.split(os.sep)[2]  # pylint: disable=E1101
        st = process_time()
        _file_list = []
        for file in os.listdir(folder):
            filename = os.fsdecode(file)
            if filename.endswith(".json"):
                _asset = os.path.join(folder, filename)
                Logger.log(f"Found Asset: {_asset}")
                _file_list.append(_asset)
            else:
                Logger.log(
                    f"{os.path.join(folder, filename)} is no valid Asset File", 2
                )
        et = process_time()
        importtime = et - st
        if importtime > 1:
            dbglevel = 2
        else:
            dbglevel = 1
        Logger.log(f"Gathering {_folder_name} took: {importtime*1000}ms", dbglevel)
        return _file_list

    def importLevels(_levels_folder: str) -> None:
        """Imports Levels from Assets

        Returns:
            None: None
        """
        _level_files = AssetHandler.getFiles(_levels_folder)

        if not _level_files:
            Logger.log(f"No Levels to import from {_levels_folder}", 1)
            return None

        st = process_time()
        Logger.log(f"Importing Level(s) from: {_level_files}", 1)

        for _level in tqdm(
            _level_files,
            desc="Importing Levels...",
            ncols=100,
            bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [ETA: {remaining_s:.2f}s]",
        ):
            AssetHandler.allLevels.extend(LevelInit.load_all_levels_from_json(_level))

        et = process_time()
        importtime = et - st
        if importtime > 1:
            dbglevel = 2
        else:
            dbglevel = 1
        Logger.log(f"Importing Levels took: {importtime*1000}ms", dbglevel)
        return None

    def importEntities(_entities_folder: str) -> None:
        """Imports Entities from Assets

        Returns:
            None: None
        """

        _entity_files = AssetHandler.getFiles(_entities_folder)

        if not _entity_files:
            Logger.log(f"No Entities to import from {_entities_folder}", 1)
            return None

        st = process_time()
        Logger.log(f"Importing Entities: {_entity_files}", 1)

        for _entity in tqdm(
            _entity_files,
            desc="Importing Entities...",
            ncols=100,
            bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [ETA: {remaining_s:.2f}s]",
        ):
            AssetHandler.allEntities.extend(EntityInit.load_entities_fromjson(_entity))

        et = process_time()
        importtime = et - st
        if importtime > 1:
            dbglevel = 2
        else:
            dbglevel = 1
        Logger.log(f"Importing Entities took: {importtime*1000}ms", dbglevel)
        return None

    def importItems(_items_folder: str) -> None:
        """Imports Items from Assets

        Returns:
            None: None
        """
        _items_files = AssetHandler.getFiles(_items_folder)

        if not _items_files:
            Logger.log(f"No Items to import from {_items_folder}", 1)
            return None

        st = process_time()
        Logger.log(f"Importing Item(s) from: {_items_files}", 1)

        for _items in tqdm(
            _items_files,
            desc="Importing Items...",
            ncols=100,
            bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [ETA: {remaining_s:.2f}s]",
        ):
            AssetHandler.allItems.extend(itemInit.load_all_items_from_json(_items))

        et = process_time()
        importtime = et - st
        if importtime > 1:
            dbglevel = 2
        else:
            dbglevel = 1
        Logger.log(f"Importing Items took: {importtime*1000}ms", dbglevel)
        return None

    def importEffects(_effects_folder: str) -> None:
        """Imports Effects from Assets

        Returns:
            None: None
        """
        _effects_files = AssetHandler.getFiles(_effects_folder)

        if not _effects_files:
            Logger.log(f"No Effects to import from {_effects_folder}", 1)
            return None

        st = process_time()
        Logger.log(f"Importing Effects: {_effects_files}")

        for _effect in tqdm(
            _effects_files,
            desc="Importing Effects...",
            ncols=100,
            bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [ETA: {remaining_s:.2f}s]",
        ):
            AssetHandler.allEffects.extend(
                EffectInit.load_all_effects_from_json(_effect)
            )

        et = process_time()
        importtime = et - st
        if importtime > 1:
            dbglevel = 2
        else:
            dbglevel = 1
        Logger.log(f"Importing Effects took: {importtime*1000}ms", dbglevel)
        return None


def load_game() -> None:
    """Function to init the whole Game"""
    rootdir = "..\\TA\\Assets".replace("\\", os.sep)
    Assetpacks = []

    # the underscore representes dirs
    for subdir, _, files in os.walk(rootdir):
        for file in files:
            filepath = subdir + os.sep + file

            if filepath.endswith("meta.conf"):
                with open(filepath, "r", encoding="UTF-8") as f:
                    json_object = json.loads(f.read())
                    Assetpacks.append(json_object)

    for _assetpack in Assetpacks:
        name = next(iter(_assetpack))
        _newAsset = Assetpack(
            name,
            _assetpack[name]["creator"],
            _assetpack[name]["version"],
            _assetpack[name]["description"],
            _assetpack[name]["root"],
            _assetpack[name]["content"],
        )
    for _assetpack in AssetHandler.Assetpacks:
        for _ctype in _assetpack.content.keys():
            match _ctype:
                case "Entities":
                    AssetHandler.importEntities(
                        _assetpack.root + "\\".replace("\\", os.sep) + _ctype
                    )
                case "Levels":
                    AssetHandler.importLevels(
                        _assetpack.root + "\\".replace("\\", os.sep) + _ctype
                    )
                case "Items":
                    AssetHandler.importItems(
                        _assetpack.root + "\\".replace("\\", os.sep) + _ctype
                    )
                case "Effects":
                    AssetHandler.importEffects(
                        _assetpack.root + "\\".replace("\\", os.sep) + _ctype
                    )
    ###Validation
    if not AssetHandler.Assetpacks:
        Logger.log("No Assetpacks found! Skipping Game init", 4)
        sys.exit()


class Assetpack:
    """Assetpacks which are loaded during Game Init containing all the Game Assets"""

    __slots__ = (
        "name",
        "creator",
        "version",
        "description",
        "root",
        "content",
        "levels",
        "entities",
        "items",
        "effects",
        "loottables",
        "ai",
        "unknown",
        "valid",
    )

    def __init__(
        self,
        name: str = "",
        creator: str = "",
        version: int = 0,
        description: str = "",
        root: str = "",
        content: dict = None,
    ) -> None:
        if content is None:
            content = {}

        self.name = name
        self.creator = creator
        self.version = version
        self.description = description
        self.root = root.replace("\\", os.sep)
        self.content = content
        self.levels = []
        self.entities = []
        self.items = []
        self.effects = []
        self.loottables = []
        self.ai = []
        self.unknown = []
        self.valid = False

        if not self.validate():
            Logger.log(f"Assetpack {self} could not be verified!", 2)

    def __str__(self) -> str:
        return f"{self.name}"

    @Logger.time
    def validate(self) -> bool:
        """Checks File SHA256 Sum
        Returns:
            Bool: True if integrity is Verified, otherwise False
        """
        errors = False
        ignore_errors = False

        for ctype in self.content.keys():
            for _file in self.content[ctype].keys():
                _filepath = (
                    self.root
                    + "\\".replace("\\", os.sep)
                    + ctype
                    + "\\".replace("\\", os.sep)
                    + _file
                )

                sha256sum = sha256()

                with open(_filepath, "rb") as f:
                    data_chunk = f.read(1024)
                    while data_chunk:
                        sha256sum.update(data_chunk)
                        data_chunk = f.read(1024)
                checksum = sha256sum.hexdigest()
                if self.content[ctype][_file] != checksum and ignore_errors is False:
                    # add choice to ignore file checking
                    if dbg:
                        print(
                            """One of your Game-Files has a wrong Hash. It may be broken!\n
                        Do you want to ignore this and further File errors? (y/n)
                        """
                        )
                        choice = input()
                        if choice == "y":
                            ignore_errors = True
                    if ignore_errors is False:
                        errors = True
                        Logger.log(
                            f"""wrong checksum for file {_file} : <{checksum}>
                            expected: <{self.content[ctype][_file]}>""",
                            2,
                        )
                else:
                    Logger.log(
                        f"Asset verified: {_file} : {checksum} = {self.content[ctype][_file]}",
                        0,
                    )
                    match ctype:
                        case "Entities":
                            self.entities.append(_file)
                        case "Items":
                            self.items.append(_file)
                        case "Effects":
                            self.effects.append(_file)
                        case "Levels":
                            self.levels.append(_file)
                        case "Loottables":
                            self.loottables.append(_file)
                        case "AI":
                            self.ai.append(_file)
                        case _:
                            self.unknown.append(_file)
        if errors:  # pylint: disable=R1705
            self.valid = False
            return False
        else:
            self.valid = True
            AssetHandler.Assetpacks.append(self)
            return True
