from pathlib import Path


def check_for_save_file():

    my_file = Path("../../rom/rom.gba")

    if my_file.is_file():
        return True
    else:
        return False
