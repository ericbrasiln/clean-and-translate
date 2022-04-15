"""Script to clean text from a file.
"""
import re
from aux_functions import *

# function to clean text
def limpar_text(text):
    """Clean text.
    """
    # find matches for the pattern \n, digit, \n 
    page_pattern = re.compile(r'\n\d+\n')
    # find all matches
    pages = page_pattern.findall(text)
    for page in pages:
        text = text.replace(page, f'[p.{page}]')
    # replace [p. \n\d{2}\n] with [p. \d{2}]
    clean_page_pattern = re.compile(r'\[p\.\n\d+\s+\]')
    clean_pages = clean_page_pattern.findall(text)
    for clean_page in clean_pages:
        if len(clean_page) == 8:
            text = text.replace(clean_page, f'[p.{clean_page[4:6]}]')
        else:
            text = text.replace(clean_page, f'[p.{clean_page[4:7]}]')
    # regex to find footnotes that start with \n, (, number, and ) and 
    # everything after until the end of the line
    fn_pattern = re.compile(r'\n\([0-9]+\)[^\n]*')
    # find all matches
    fns = fn_pattern.findall(text)
    # add it to a list
    fns = list(fns)
    # remove all matches from text
    for fn in fns:
        text = text.replace(fn, '')
    text = text.replace('-\n', '')
    # find pattern \n, strings and remove \n 
    text = text.replace('\t', ' ')
    text = text.replace('\n\n', '\n')
    # append matches in the end of the text
    text = text + '\n'.join(fns)
    return text

raw_text = 'raw_txt/lecture de Darwin.txt'
clean_text = 'clean_txt/lecture_de_darwin.txt'

# call functions
read_save(raw_text, limpar_text, clean_text)
