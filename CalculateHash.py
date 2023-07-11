from hashlib import sha256
import os
from pathlib import Path


def get_project_root() -> Path:
    """Returns Root path of Project

    Returns:
        Path: Path to Root Dir
    """
    return Path(__file__).parent.parent


root_folder = get_project_root()


def check_integrity(file):
    """Checks File SHA256 Sum against Integrity File

    Args:
        file (path): File to Check

    Returns:
        Bool: True if integrity is Verified, otherwise False
    """

    # Calculates SHA256 Checksum for given File
    sha256sum = sha256()
    with open(file, "rb") as f:
        data_chunk = f.read(1024)
        while data_chunk:
            sha256sum.update(data_chunk)
            data_chunk = f.read(1024)

    checksum = sha256sum.hexdigest()

    # Checks if Calculated Checksum is in Checksums File
    return checksum


def CheckGameIntegrity():
    """Checks game Files for Integrity"""
    _gameFiles = []
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
                _gameFiles.append(os.path.join(root, name))
    with open("./config/integrity.md", "w", encoding="UTF-8") as integrityfile:
        for gfile in _gameFiles:
            integrityfile.write(check_integrity(gfile) + "\n")


CheckGameIntegrity()
