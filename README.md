# find-and-replace-in-epub

This is a simple python script that finds and replaces word(s) in .epub files. 

## Usage:
```python main.py <csv_file> <source_path> -o <destination_path>```  

For example, ```python main.py replace.csv input.epub output.epub```
### Command-line arguements:

#### csv_file  
Specify the words in two fields in a csv file with first line being 'find,replace'   
```csv
find,replace
one word, another word
Apple,Banana
```
Note that replacements are case-sensitive so Apple,Banana will replace 'Apple' with Banana but won't alter 'apple'.

#### source_path
Path of the original .epub file to replace words from. The original .epub file will not be modified.  
The path can be relative or absolute or just the name of the file if it is present in the current directory.  

#### destination_path
The (optional) name of the modified epub file you want to save. Specify with flag ```-o <filepath>``` A new epub file will be created at the specified path. By default saves at epub/output.epub.
