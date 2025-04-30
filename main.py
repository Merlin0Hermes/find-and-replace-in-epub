import os
import sys
import csv
import re
import argparse
import platform
from ebooklib import epub
from bs4 import BeautifulSoup
from typing import Dict


def clear_terminal():
    if platform.system == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def dict_from_csv(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        return {row["find"]: row["replace"] for row in reader}


def find_and_replace(words_dict, input_epub, output_epub):

    pattern = re.compile('|'.join(re.escape(key) for key in words_dict.keys()))

    book = epub.read_epub(input_epub)
    i = 1
    for item in book.get_items():

        if (isinstance(item, epub.EpubHtml)):
            soup = BeautifulSoup(item.get_body_content(), 'html.parser')

            def replace_words(text):
                return pattern.sub(lambda match: words_dict[match.group(0)], text)
                
            for text in soup.find_all(string=True):
                new_text = replace_words(text)
                text.replace_with(new_text)
            
            item.set_content(str(soup))

            clear_terminal()
            print(f"Progress: Chapter {i}")
            i += 1

    epub.write_epub(output_epub, book)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("replace_csv", help="path to csv file with find,replace values")
    parser.add_argument("source", help="path to the source/input epub file")
    parser.add_argument("-o", "--output", help="path (or name) to save the output epub, defaults to output.epub")
    
    args = parser.parse_args()
    words_dict = dict_from_csv(args.replace_csv)
    input_epub = args.source
    if (args.output):
        output_epub = args.output
    else:
        output_epub = "output.epub"

    find_and_replace(words_dict, input_epub, output_epub)


if __name__ == "__main__":
    main()
