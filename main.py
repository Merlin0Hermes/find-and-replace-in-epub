import argparse
from ebooklib import epub
from bs4 import BeautifulSoup

from utils import * # user defined functions


def find_and_replace(words_dict, input_epub, output_epub):

    pattern = get_pattern(words_dict) # function from utils.py

    book = epub.read_epub(input_epub)
    i = 1
    for item in book.get_items():

        if (isinstance(item, epub.EpubHtml)):
            soup = BeautifulSoup(item.get_body_content(), 'html.parser')
                
            for text in soup.find_all(string=True):
                new_text = replace_words(text, pattern, words_dict) # function from utils.py
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
    parser.add_argument("-o", "--output", help="path (or name) to save the output epub, defaults to epub/output.epub")
    parser.add_argument("-w", "--whitespace", action="store_true",
                        help="does not ignore the leading and trailing whitespace in the csv file. (overrides default behaviour of"
                         + " stripping away whitespace)")
    
    args = parser.parse_args()
    words_dict = dict_from_csv(Path(args.replace_csv), args.whitespace)
    input_epub = Path(args.source)

    if (args.output):
        output_epub = Path(args.output)
    else:
        path = make_directory("epub")
        output_epub = path / f"{input_epub.stem}-new.epub"
        print(output_epub)

    find_and_replace(words_dict, input_epub, output_epub)


if __name__ == "__main__":
    main()
