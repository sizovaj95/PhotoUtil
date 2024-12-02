import os
from pathlib import Path

import PIL
from PIL import Image
import re
from pillow_heif import register_heif_opener


path = Path(r"D:\Julia\Documents\Photos\Gwydir2024")  #Path(__file__).parent.resolve() / "test_files"

register_heif_opener()


def convert_from_heic(file, remove_heic: bool = False):
    new_name = re.sub(r"\.[Hh][Ee][Ii][Cc]$", ".jpg", file.name)
    try:
        heic_im = Image.open(file.path)
    except PIL.UnidentifiedImageError as e:
        print(e)
        return
    try:
        heic_im.convert("RGB").save(path / new_name)
    except Exception as e:
        print(e)
        return
    if remove_heic:
        try:
            os.remove(file.path)
        except Exception as e:
            print(e)


def main():
    if not os.path.exists(path):
        print(f"Folder {path} does not exist!")
    files = list(os.scandir(path))
    for file in files:
        if re.search(r"\.heic$", file.name, re.I):
            convert_from_heic(file, True)


if __name__ == "__main__":
    main()
