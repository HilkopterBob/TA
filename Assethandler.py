"""Assethandler for importing needed Assets
"""

import os
import sys
import json
from hashlib import sha256
from time import sleep, process_time
from tqdm import tqdm
from Level import LevelInit
from Entities import EntityInit
from Effect import EffectInit
from Items import itemInit
from config import (
    checksum_file,
    dbg,
    root_folder,
)
from Utils.pr import Pr
from Utils import Debug, Logger


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

    def getFiles(
        folder,
    ):  # ToDo: Files are Gathered twice because of new Assetpack structure; Change GetFiles so it does not Gather Files but instead reads from Assetpack where the Files are
        """Gets all Json Files from a Folder

        Args:
            folder (Path): Path to Folder to look for Files

        Returns:
            List: List of Paths to Files
        """
        Logger.log(f"Gathering Assets from: {folder}", 1)
        _folder_name = folder.split("\\")[2]  # pylint: disable=E1101
        st = process_time()
        _file_list = []
        for file in os.listdir(folder):
            filename = os.fsdecode(file)
            if filename.endswith(".json"):
                _asset = os.path.join(folder, filename)
                if AssetHandler.check_integrity(_asset):
                    Logger.log(f"Found Asset: {_asset}")
                    _file_list.append(_asset)
                else:
                    Debug.stop_game_on_exception("File Integrity Check Failed")
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

    def importLevels(_levels_folder):
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

    def importEntities(_entities_folder):
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

    def importItems(_items_folder):
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

    def importEffects(_effects_folder):
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

    def check_integrity(file):
        """Checks File SHA256 Sum against Integrity File

        Args:
            file (path): File to Check

        Returns:
            Bool: True if integrity is Verified, otherwise False
        """
        # Skip Integrity Check if Debug Mode is Enabled
        if dbg:
            return True

        # Read checksums_file from Config and saves Checksums
        checksums = []
        with open(checksum_file, "r", encoding="utf-8") as f:
            checksums = [line.strip() for line in f.readlines()]

        # Calculates SHA256 Checksum for given File
        sha256sum = sha256()
        with open(file, "rb") as f:
            data_chunk = f.read(1024)
            while data_chunk:
                sha256sum.update(data_chunk)
                data_chunk = f.read(1024)

        checksum = sha256sum.hexdigest()

        # Checks if Calculated Checksum is in Checksums File
        if checksum not in checksums:
            Logger.log(f"Integrity Check Failed for File: {file}", 2)
            Logger.log(f"Checksum of File {file}: {checksum}")
            return False
        return True

    def CheckGameIntegrity():
        """Checks game Files for Integrity"""
        _modFiles = []
        _DLCFiles = []
        _coreFiles = []
        _success = 0
        exclude = [
            ".git",
            ".github",
            ".vscode",
            "logs",
            "__pycache__",
            "pypi",
            "Docs",
            "releases",
        ]
        excludef = ["integrity.md"]
        for root, dirs, files in os.walk(root_folder, topdown=True):
            dirs[:] = [d for d in dirs if d not in exclude]
            for name in files:
                if name not in excludef:
                    if "DLC" in root:
                        _DLCFiles.append(os.path.join(root, name))
                    elif "Mods" in root:
                        _modFiles.append(os.path.join(root, name))
                    else:
                        _coreFiles.append(os.path.join(root, name))
        with tqdm(
            total=len(_coreFiles) + len(_DLCFiles) + len(_modFiles),
            desc="Checking File Integrity...",
            ncols=100,
            bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [ETA: {remaining_s:.2f}s]",
        ) as progress:
            for gfile in _coreFiles:
                sleep(0.02)
                if AssetHandler.check_integrity(gfile):
                    progress.update()
                else:
                    # Go on or break
                    progress.update()
                    _success = 1
            for gfile in _DLCFiles:
                sleep(0.1)
                if AssetHandler.check_integrity(gfile):
                    progress.update()
                else:
                    # Go on or break
                    progress.update()
                    _success = 2
                    # Debug.stop_game_on_exception("File Integrity Check Failed")
                    # -> Output DLC wurde gefunden aber Files corrupt
                    # -> Möchtest du das spiel ohne DLC starten
                    # -> DLC nicht in enabled Flags aufnehmen
            for gfile in _modFiles:
                sleep(0.1)
                if AssetHandler.check_integrity(gfile):
                    progress.update()
                else:
                    # Go on or break
                    progress.update()
                    _success = 3
                    # Debug.stop_game_on_exception("File Integrity Check Failed")
        if dbg:
            _success = 0
        match _success:
            case 0:
                Logger.log("File Integrity Check passed", 1)
            case 1:
                Logger.log("Critical Error on integrity Check. Exiting Game!", 2)
                Pr.red(
                    "File Integrity Check failed. See Logs for Errors. Exiting Game..."
                )
                sys.exit()
            case 2:
                Logger.log("DLC Error", 2)
                Pr.red("DLC Integrity Check failed. See Logs for Errors.")
                Debug.stop_game()
            case 3:
                Logger.log("MOD Error", 2)
                Pr.red("MOD Integrity Check failed. See Logs for Errors.")
                Debug.stop_game()


def load_game():
    """Function to init the whole Game; TODO: Build this"""
    rootdir = "..\\TA\\Assets"
    Assetpacks = []
    for subdir, dirs, files in os.walk(rootdir):
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
                    AssetHandler.importEntities(_assetpack.root + "\\" + _ctype)
                case "Levels":
                    AssetHandler.importLevels(_assetpack.root + "\\" + _ctype)
                case "Items":
                    AssetHandler.importItems(_assetpack.root + "\\" + _ctype)
                case "Effects":
                    AssetHandler.importEffects(_assetpack.root + "\\" + _ctype)


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
        self, name="", creator="", version=0, description="", root="", content=None
    ):
        if content is None:
            content = {}

        self.name = name
        self.creator = creator
        self.version = version
        self.description = description
        self.root = root
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
            return

    def __str__(self):
        return f"{self.name}"

    @Logger.time
    def validate(self):
        """Checks File SHA256 Sum
        Returns:
            Bool: True if integrity is Verified, otherwise False
        """
        errors = False

        for ctype in self.content.keys():
            for _file in self.content[ctype].keys():
                _filepath = self.root + "\\" + ctype + "\\" + _file

                sha256sum = sha256()

                with open(_filepath, "rb") as f:
                    data_chunk = f.read(1024)
                    while data_chunk:
                        sha256sum.update(data_chunk)
                        data_chunk = f.read(1024)
                checksum = sha256sum.hexdigest()
                if self.content[ctype][_file] != checksum:
                    errors = True
                    Logger.log(
                        f"Checksum wrong for file {_file} : <{checksum}> expected: <{self.content[ctype][_file]}>",
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
        if errors:
            self.valid = False
            return False
        else:
            self.valid = True
            AssetHandler.Assetpacks.append(self)
            return True
