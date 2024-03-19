"""Configuration for Textadventure
"""

import sys
import os.path
import os
from datetime import date
from pathlib import Path
from Utils.tcolors import white, red, yellow, purple, cyan, green

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
dbg_level = (
    0  # 0 ERR only | #1 WARN + ERR | #2 INFO + WARN + ERR | #3 DBG + INFO + WARN + ERR
)
exclude_dbg_lvl = True
sys.stdout.reconfigure(encoding="utf-8")
logbymodule = True
##################

####################
# New Logging Module#
logging = True  # Enable Logging
fileLogging = True  # Enables Logging to File
consoleLogging = True  # Enable Logging Output in Console
LogByModule = False  # Create a Logfile for each Module only
ShowOnlyLogText = True  # Only Prints the Log Text(colored) in Console

logLevels = {
    -1: "DBG",
    0: "TRACE",
    1: "INFO",
    2: "WARN",
    3: "ERR",
    4: "FATAL",
}  # Define of Loglevels

DefaultLogLevel = -1

consoleLogLevel = (
    -1  # Choose Log Level shown in Console (Higher Levels are always included)
)

FileLogLevel = (
    -1  # Choose the Log Level for File Output (Higher Levels are always included)
)

LogColors = {
    -1: purple,
    0: cyan,
    1: white,
    2: yellow,
    3: red,
    4: red,
}  # Color Definition

LogPrefix = {
    -1: f'{purple("[~]")} {purple("[+]")} {white("-")}',
    0: f'{cyan("[~]")} {cyan("[~]")} {white("-")}',
    1: f'{green("[~]")} {green("[+]")} {white("-")}',
    2: f'{yellow("[!]")} {yellow("[!]")} {white("-")}',
    3: f'{yellow("[!]")} {red("[-]")} {white("-")}',
    4: f'{red("[!]")} {red("[!]")} {white("-")}',
}  # Prefix for InConsole Logging

####################


##################
###ENV Variables##
items_file = "config\\items.json".replace("\\", os.sep)
effects_file = "config\\effects.json".replace("\\", os.sep)
entities_folder = "Assets\\Core\\Entities".replace("\\", os.sep)  # TODO: Remove
items_folder = "Assets\\Core\\Items".replace("\\", os.sep)  # TODO: Remove
loottablepath = "Assets\\Core\\Loottables".replace("\\", os.sep)  # TODO: Remove
aitablepath = "Assets\\Core\\AI".replace("\\", os.sep)
log_file = f"logs\\{today}.log".replace("\\", os.sep)
root_folder = get_project_root()
##################

##################
### Config Vars ##
##################
max_processes = os.cpu_count()

##################
##Log File Check##
if not os.path.exists(log_file):
    try:
        with open(log_file, mode="a", encoding="UTF-8"):
            pass
    except Exception as e:
        print(f"ERR creating Logfile: {e}")
##################
