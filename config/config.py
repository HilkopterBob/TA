"""Configuration for Textadventure
"""
import sys
import os.path
from datetime import date

##################
#####Init Vars####
today = date.today().strftime('%d-%m-%Y')
##################

##################
##Debug Variable##
dbg = True
dbg_level = 2            #0 ERR only | #1 WARN + ERR | #2 INFO + WARN + ERR
sys.stdout.reconfigure(encoding='utf-8')
#hunter.trace(module="__main__")
##################

##################
###ENV Variables##
items_file = "config/items.json"
levels_file = "config/levels.json"
effects_file = "config/effects.json"
entity_file = "config/entities.json"
log_file = f"logs/{today}.log"
##################

##################
##Log File Check##
if not os.path.exists(log_file):
    try:
        with open(log_file, mode='a', encoding='UTF-8'):
            pass
    except Exception as e:
        print(f'ERR creating Logfile: {e}')
##################
