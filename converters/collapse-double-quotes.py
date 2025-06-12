#To run this file, use this command: python collapse_quotes.py raw.csv cleaned.csv
#You can add a third argument if you want the files encoded in a specific way.

#This file exists to remove double quotes from the resulting csvfiles of the converters from json to csv

import re
import argparse

#Collapse any literal "" → "
collapse_re = re.compile(r'""')

#Convert JSON-like lists to semicolon-lists
list_re = re.compile(r'\[\s*"([^"]*?)"(?:\s*,\s*"([^"]*?)")*?\s*\]')

def collapse_and_unjsonify(line: str) -> str:
    #Collapse "" → "
    line = collapse_re.sub(r'"', line)

    #For every [ "x", "y", ... ], strip [ ] and quotes, join with '; '
    def repl(m):
        #m.group(0) full match; m.groups() is dynamic
        items = re.findall(r'"([^"]*?)"', m.group(0))
        return '; '.join(items)
    
    return list_re.sub(repl, line)

def process_file(input_path: str, output_path: str, encoding: str = 'utf-8'):
    with open(input_path, 'r', encoding=encoding) as fin:
        lines = fin.readlines()
    with open(output_path, 'w', encoding=encoding) as fout:
        for line in lines:
            fout.write(collapse_and_unjsonify(line))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Collapse double-quotes and turn JSON-lists into ';'-lists for Bubble CSV import"
    )
    parser.add_argument('input_csv',  help='Path to raw CSV')
    parser.add_argument('output_csv', help='Path to cleaned CSV')
    parser.add_argument(
        '--encoding', default='utf-8',
        help='File encoding (default: utf-8)'
    )
    args = parser.parse_args()
    process_file(args.input_csv, args.output_csv, args.encoding)
