import os
import csv
import platform
from pathlib import Path

def make_directory(dir_name):
    try:
        Path(dir_name).mkdir(parents=True, exist_ok=True)
        return Path(dir_name)
    except Exception as e:
        print(f"An error occured {e}")


def clear_terminal():
    if platform.system == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def dict_from_csv(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        return {row["find"]: row["replace"] for row in reader}