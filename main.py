import os
import sys
import csv
from ebooklib import epub
from bs4 import BeautifulSoup
from typing import Dict


def dict_from_csv(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        return {row["find"]: row["replace"] for row in reader}


def find_and_replace(words_dict, input_epub, output_epub):
   
    book = epub.read_epub(input_epub)
    i = 1
    for item in book.get_items():

        if (isinstance(item, epub.EpubHtml)):
            soup = BeautifulSoup(item.get_body_content(), 'html.parser')

            for old_word, new_word in words_dict.items():
                for text in soup.find_all(string=True):
                    new_text = text.replace(old_word, new_word)
                    text.replace_with(new_text)
            
            item.set_content(str(soup))

            os.system("clear")
            print(f"Progress: Chapter {i}")
            i += 1

    epub.write_epub(output_epub, book)



def main():
    
    words_dict = dict_from_csv(sys.argv[1])
    input_epub = sys.argv[2]
    output_epub = sys.argv[3]  

    find_and_replace(words_dict, input_epub, output_epub)


if __name__ == "__main__":
    main()
