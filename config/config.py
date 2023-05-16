"""Configuration for Textadventure
"""
import sys
import os.path
from datetime import date
from pathlib import Path


##################
#####Init Vars####
today = date.today().strftime("%d-%m-%Y")
##################


##################
##Init Functions##
def get_project_root() -> Path:
    """Returns Root path of Project

    Returns:
        Path: Path to Root Dir
    """
    return Path(__file__).parent.parent


##################

##################
##Debug Variable##
dbg = True
dbg_level = 2  # 0 ERR only | #1 WARN + ERR | #2 INFO + WARN + ERR
sys.stdout.reconfigure(encoding="utf-8")
# hunter.trace(module="__main__")
##################

##################
###ENV Variables##
items_file = "config/items.json"
effects_file = "config/effects.json"
levels_folder = "Assets/Levels"
entities_folder = "Assets/Entities"
effects_folder = "Assets/Effects"
log_file = f"logs/{today}.log"
checksum_file = "config/integrity.md"
root_folder = get_project_root()
##################


##################
##Log File Check##
if not os.path.exists(log_file):
    try:
        with open(log_file, mode="a", encoding="UTF-8"):
            pass
    except Exception as e:
        print(f"ERR creating Logfile: {e}")
##################
