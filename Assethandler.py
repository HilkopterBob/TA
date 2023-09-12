"""Assethandler for importing needed Assets
"""
import os
import sys
from hashlib import sha256
from time import sleep, process_time
from progress.bar import Bar
from Level import LevelInit
from Entities import EntityInit
from Effect import EffectInit
from Items import itemInit
from config import (
    levels_folder,
    entities_folder,
    effects_folder,
    items_folder,
    checksum_file,
    dbg,
    root_folder,
)
from Utils.pr import Pr
from Utils import Debug


class AssetHandler:
    """Handles import of Assets from Assets Folder

    Returns:
        None: None
    """

    allLevels = []
    allEntities = []
    allEffects = []
    allItems = []

    def getFiles(folder):
        """Gets all Json Files from a Folder

        Args:
            folder (Path): Path to Folder to look for Files

        Returns:
            List: List of Paths to Files
        """
        Pr.dbg(f"Gathering Assets from: {folder}")
        # TODO: find out the problem pylint has
        _folder_name = folder.split("/")[2]  # pylint: disable=E1101
        st = process_time()
        _file_list = []
        for file in os.listdir(folder):
            filename = os.fsdecode(file)
            if filename.endswith(".json"):
                _asset = os.path.join(folder, filename)
                if AssetHandler.check_integrity(_asset):
                    Pr.dbg(f"Found Asset: {_asset}")
                    _file_list.append(_asset)
                else:
                    Debug.stop_game_on_exception("File Integrity Check Failed")
            else:
                Pr.dbg(f"{os.path.join(folder, filename)} is no valid Asset File", 2)
        et = process_time()
        importtime = et - st
        if importtime > 1:
            dbglevel = 2
        else:
            dbglevel = 1
        Pr.dbg(f"Gathering {_folder_name} took: {importtime*1000}ms", dbglevel)
        return _file_list

    def importLevels():
        """Imports Levels from Assets

        Returns:
            None: None
        """
        _level_files = AssetHandler.getFiles(levels_folder)

        if not _level_files:
            Pr.dbg(f"No Levels to import from {levels_folder}", 1)
            return None

        st = process_time()
        Pr.dbg(f"Importing Level(s) from: {_level_files}")
        with Bar(
            "Importing Levels...",
            suffix="%(percent).1f%% - ETA: %(eta)ds",
            max=len(_level_files),
        ) as progress:
            for _level in _level_files:
                AssetHandler.allLevels.extend(
                    LevelInit.load_all_levels_from_json(_level)
                )
                progress.next()
        et = process_time()
        importtime = et - st
        if importtime > 1:
            dbglevel = 2
        else:
            dbglevel = 1
        Pr.dbg(f"Importing Levels took: {importtime*1000}ms", dbglevel)
        return None

    def importEntities():
        """Imports Entities from Assets

        Returns:
            None: None
        """

        _entity_files = AssetHandler.getFiles(entities_folder)

        if not _entity_files:
            Pr.dbg(f"No Entities to import from {entities_folder}", 1)
            return None

        st = process_time()
        Pr.dbg(f"Importing Entities: {_entity_files}")
        with Bar(
            "Importing Entities...",
            suffix="%(percent).1f%% - ETA: %(eta)ds",
            max=len(_entity_files),
        ) as progress:
            for _entity in _entity_files:
                AssetHandler.allEntities.extend(
                    EntityInit.load_entities_fromjson(_entity)
                )
                progress.next()
        et = process_time()
        importtime = et - st
        if importtime > 1:
            dbglevel = 2
        else:
            dbglevel = 1
        Pr.dbg(f"Importing Entities took: {importtime*1000}ms", dbglevel)
        return None

    def importItems():
        """Imports Items from Assets

        Returns:
            None: None
        """
        _items_files = AssetHandler.getFiles(items_folder)

        if not _items_files:
            Pr.dbg(f"No Items to import from {items_folder}", 1)
            return None

        st = process_time()
        Pr.dbg(f"Importing Item(s) from: {_items_files}")
        with Bar(
            "Importing Items...",
            suffix="%(percent).1f%% - ETA: %(eta)ds",
            max=len(_items_files),
        ) as progress:
            for _items in _items_files:
                AssetHandler.allItems.extend(itemInit.load_all_items_from_json(_items))
                progress.next()
        et = process_time()
        importtime = et - st
        if importtime > 1:
            dbglevel = 2
        else:
            dbglevel = 1
        Pr.dbg(f"Importing Items took: {importtime*1000}ms", dbglevel)
        return None

    def importEffects():
        """Imports Effects from Assets

        Returns:
            None: None
        """
        st = process_time()
        _effects_files = AssetHandler.getFiles(effects_folder)

        if not _effects_files:
            Pr.dbg(f"No Effects to import from {effects_folder}", 1)
            return None

        Pr.dbg(f"Importing Effects: {_effects_files}")

        for _effect in _effects_files:
            AssetHandler.allEffects.extend(
                EffectInit.load_all_effects_from_json(_effect)
            )
        et = process_time()
        importtime = et - st
        if importtime > 1:
            dbglevel = 2
        else:
            dbglevel = 1
        Pr.dbg(f"Importing Effects took: {importtime*1000}ms", dbglevel)
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
            Pr.dbg(f"Integrity Check Failed for File: {file}", 2)
            Pr.dbg(f"Checksum of File {file}: {checksum}")
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
        with Bar(
            "Checking File integrity...",
            suffix="%(percent).1f%% - ETA: %(eta)ds",
            max=len(_coreFiles) + len(_DLCFiles) + len(_modFiles),
        ) as progress:
            for gfile in _coreFiles:
                sleep(0.02)
                if AssetHandler.check_integrity(gfile):
                    progress.next()
                else:
                    # Go on or break
                    progress.next()
                    _success = 1
            for gfile in _DLCFiles:
                sleep(0.1)
                if AssetHandler.check_integrity(gfile):
                    progress.next()
                else:
                    # Go on or break
                    progress.next()
                    _success = 2
                    # Debug.stop_game_on_exception("File Integrity Check Failed")
                    # -> Output DLC wurde gefunden aber Files corrupt
                    # -> Möchtest du das spiel ohne DLC starten
                    # -> DLC nicht in enabled Flags aufnehmen
            for gfile in _modFiles:
                sleep(0.1)
                if AssetHandler.check_integrity(gfile):
                    progress.next()
                else:
                    # Go on or break
                    progress.next()
                    _success = 3
                    # Debug.stop_game_on_exception("File Integrity Check Failed")
        if dbg:
            _success = 0
        match _success:
            case 0:
                Pr.dbg("File Integrity Check passed", 1)
            case 1:
                Pr.dbg("Critical Error on integrity Check. Exiting Game!", 2)
                Pr.red(
                    "File Integrity Check failed. See Logs for Errors. Exiting Game..."
                )
                sys.exit()
            case 2:
                Pr.dbg("DLC Error", 2)
                Pr.red("DLC Integrity Check failed. See Logs for Errors.")
                Debug.stop_game()
            case 3:
                Pr.dbg("MOD Error", 2)
                Pr.red("MOD Integrity Check failed. See Logs for Errors.")
                Debug.stop_game()


def load_game():
    pass
