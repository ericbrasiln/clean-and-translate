"""Script to clean text from a file.
"""
import re
from aux_functions import *

# function to clean text
def limpar_text(text):
    """Clean text.
    """
    # find matches for pattern 
    odd_pattern = re.compile(r'\d+ META, LXI, HORS SÉRIE, 2016')
    odd_pattern_matches = odd_pattern.findall(text)
    for odd_page in odd_pattern_matches:
        text = text.replace(odd_page, f'[p. {odd_page[0:3]}]')
    # find matches for pattern
    even_pattern = re.compile(r'LES TRADUCTIONS FRANÇAISES DE ON THE ORIGIN OF SPECIES DE DARWIN \d+')
    even_pattern_matches = even_pattern.findall(text)
    for even_page in even_pattern_matches:
        text = text.replace(even_page, f'[p. {even_page[-3:]}]')
    text = text.replace('-\n', '')
    text = text.replace('\t', ' ')
    return text

raw_text = 'raw_txt/les traductions françaises de origin.txt'    
clean_text = 'clean_txt/les traductions françaises de origin.txt'

# call functions
read_save(raw_text, limpar_text, clean_text)
