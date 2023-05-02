"""Assethandler for importing needed Assets
"""
import os
from Level import LevelInit
from Entities import EntityInit
from Effect import EffectInit
from config import levels_folder, entities_folder, effects_folder
from Utils import pr


class AssetHandler:
    """ImportLevel"""

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
                pr.dbg(f"Found Asset: {_asset}")
                _file_list.append(_asset)
            else:
                pr.dbg(f"{os.path.join(folder, filename)} is no valid Asset File", 1)
        return _file_list

    def importLevels():
        """_summary_"""
        _level_files = AssetHandler.getFiles(levels_folder)

        if not _level_files:
            pr.dbg(f"No Levels to import from {levels_folder}", 1)
            return None

        pr.dbg(f"Importing Level(s) from: {_level_files}")
        for _level in _level_files:
            AssetHandler.allLevels.extend(LevelInit.load_all_levels_from_json(_level))

    def importEntities():
        """_summary_"""
        _entity_files = AssetHandler.getFiles(entities_folder)

        if not _entity_files:
            pr.dbg(f"No Entities to import from {entities_folder}", 1)
            return None

        pr.dbg(f"Importing Entities: {_entity_files}")

        for _entity in _entity_files:
            AssetHandler.allEntities.extend(EntityInit.load_entities_fromjson(_entity))

    def importEffects():
        """_summary_"""
        _effects_files = AssetHandler.getFiles(effects_folder)

        if not _effects_files:
            pr.dbg(f"No Effects to import from {effects_folder}", 1)
            return None

        pr.dbg(f"Importing Effects: {_effects_files}")

        for _effect in _effects_files:
            AssetHandler.allEffects.extend(
                EffectInit.load_all_effects_from_json(_effect)
            )
