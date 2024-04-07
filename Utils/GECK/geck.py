"""
Textadventure Utility Software.
"""

# pylint: disable=wrong-import-position
# pylint: disable=redefined-outer-name
# pylint: disable=invalid-name
# pylint: disable=redefined-builtin
# ████████████████████████████████████████ ModuleFinder ████████████████████████████████████████

import os
import platform
import glob

MODULE_FILES = []


def get_python_files():
    """gets all files from the modules sub directory.
    Returns a list of all paths as \" MODULE_FILES  \" """
    python_files = []

    python_files = [  # pylint: disable=R1721
        f for f in glob.glob("Utils/GECK/modules/*.py")  # pylint: disable=R1721
    ]  # pylint: disable=R1721

    for pyfile in python_files:
        MODULE_FILES.append(pyfile)
    return MODULE_FILES


# ████████████████████████████████████████ ModuleFinder ████████████████████████████████████████

# ████████████████████████████████████████ FilenameExtractor ███████████████████████████████████████


def get_filenames(file_paths: list):
    """extracts filenames from path"""
    system = platform.system()
    FILE_NAMES = []

    for _file in file_paths:
        if system == "Windows":
            FILE_NAMES.append(os.path.basename(_file).split(".")[0])
        else:
            FILE_NAMES.append(os.path.basename(_file).rsplit(".", 1)[0])

    return FILE_NAMES


# ████████████████████████████████████████ FilenameExtractor ███████████████████████████████████████

# ████████████████████████████████████████ ModuleLoader ████████████████████████████████████████

import importlib.util


def call_function(file_path, function_name, *args, **kwargs):  # pylint: disable=R1710
    """calls functions with filepaths and functionnames (filename)"""
    try:
        spec = importlib.util.spec_from_file_location("module_name", file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        function = getattr(module, function_name)
        return function(*args, **kwargs)
    except (ImportError, AttributeError) as e_error:
        print(
            f"Error calling function '{function_name}' from file '{file_path}': {e_error}"
        )


# ████████████████████████████████████████ ModuleLoader ████████████████████████████████████████

# ████████████████████████████████████████ GUI ████████████████████████████████████████

# from rich import print
from rich.prompt import Prompt

module_file_paths = get_python_files()
module_files = get_filenames(module_file_paths)


ASCII_ART = r"""
_____/\\\\\\\\\\\\________/\\\\\\\\\\\\\\\______________/\\\\\\\\\________/\\\________/\\\_______
 ___/\\\//////////________\/\\\///////////____________/\\\////////________\/\\\_____/\\\//________
  __/\\\___________________\/\\\_____________________/\\\/_________________\/\\\__/\\\//___________
   _\/\\\____/\\\\\\\_______\/\\\\\\\\\\\____________/\\\___________________\/\\\\\\//\\\___________
    _\/\\\___\/////\\\_______\/\\\///////____________\/\\\___________________\/\\\//_\//\\\__________
     _\/\\\_______\/\\\_______\/\\\___________________\//\\\__________________\/\\\____\//\\\_________
      _\/\\\_______\/\\\_______\/\\\____________________\///\\\________________\/\\\_____\//\\\________
       _\//\\\\\\\\\\\\/___/\\\_\/\\\\\\\\\\\\\\\__/\\\____\////\\\\\\\\\__/\\\_\/\\\______\//\\\__/\\\_
        __\////////////____\///__\///////////////__\///________\/////////__\///__\///________\///__\///__

                        --- G a r d e n   o f   E d e n   C r e a t i o n   K i t  ---
"""

print(ASCII_ART)
print("\n\nModules:")

for index, module in enumerate(module_files):
    print(f"[{index + 1}.] {module.replace('_', ' ')}")
available_choices = []
for index, thing in enumerate(module_files):
    available_choices.append(str(index + 1))

choice = (
    int(Prompt.ask("Choose wich tool do you want to load:", choices=available_choices))
    - 1
)

module_to_load = module_files[choice]

for index, file_path in enumerate(module_file_paths):
    if module_to_load in file_path:
        print(module_to_load)
        call_function(file_path, module_to_load)


# ████████████████████████████████████████ GUI ████████████████████████████████████████
