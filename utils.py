import os
import re
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


def dict_from_csv(filename, whitespace=False):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        if (whitespace):
            return {row["find"]: row["replace"] for row in reader}
        else:
            return {row["find"].strip(): row["replace"].strip() for row in reader}



def get_pattern(words_dict):
    return re.compile('|'.join(re.escape(key) for key in words_dict.keys()))


def replace_words(text, pattern, words_dict):
    return pattern.sub(lambda match: words_dict[match.group(0)], text)