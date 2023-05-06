"""Assethandler for importing needed Assets
"""
import os
from hashlib import sha256
from Level import LevelInit
from Entities import EntityInit
from Effect import EffectInit
from config import levels_folder, entities_folder, effects_folder, checksum_file, dbg
from Utils import pr, Debug


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
        pr.dbg(f"Gathering Assets from: {folder}")
        _file_list = []
        for file in os.listdir(folder):
            filename = os.fsdecode(file)
            if filename.endswith(".json"):
                _asset = os.path.join(folder, filename)
                if AssetHandler.check_integrity(_asset):
                    pr.dbg(f"Found Asset: {_asset}")
                    _file_list.append(_asset)
                else:
                    Debug.stop_game_on_exception("File Integrity Check Failed")
            else:
                pr.dbg(f"{os.path.join(folder, filename)} is no valid Asset File", 1)
        return _file_list

    def importLevels():
        """Imports Levels from Assets

        Returns:
            None: None
        """
        _level_files = AssetHandler.getFiles(levels_folder)

        if not _level_files:
            pr.dbg(f"No Levels to import from {levels_folder}", 1)
            return None

        pr.dbg(f"Importing Level(s) from: {_level_files}")
        for _level in _level_files:
            AssetHandler.allLevels.extend(LevelInit.load_all_levels_from_json(_level))

    def importEntities():
        """Imports Entities from Assets

        Returns:
            None: None
        """
        _entity_files = AssetHandler.getFiles(entities_folder)

        if not _entity_files:
            pr.dbg(f"No Entities to import from {entities_folder}", 1)
            return None

        pr.dbg(f"Importing Entities: {_entity_files}")

        for _entity in _entity_files:
            AssetHandler.allEntities.extend(EntityInit.load_entities_fromjson(_entity))

    def importEffects():
        """Imports Effects from Assets

        Returns:
            None: None
        """
        _effects_files = AssetHandler.getFiles(effects_folder)

        if not _effects_files:
            pr.dbg(f"No Effects to import from {effects_folder}", 1)
            return None

        pr.dbg(f"Importing Effects: {_effects_files}")

        for _effect in _effects_files:
            AssetHandler.allEffects.extend(
                EffectInit.load_all_effects_from_json(_effect)
            )

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
            pr.dbg(f"Integrity Check Failed for File: {file}", 2)
            pr.dbg(f"Checksum of File {file}: {checksum}")
            return False
        return True
