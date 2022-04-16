"""Script to clean text from a file.
"""
import re
from aux_functions import *

# function to clean text
def limpar_text(text):
    """Clean text.
    """
    # find matches for the pattern '\d{3} SÉANCE DU 2 OCTOBRE 1890.' 
    odd_pattern = re.compile(r'\d{3} SÉANCE DU 2 OCTOBRE 1890.')
    odd_pattern_matches = odd_pattern.findall(text)
    for odd_page in odd_pattern_matches:
        text = text.replace(odd_page, f'[p. {odd_page[0:3]}]')
    # find matches for the pattern 'DISCUSSION SUR LA DÉPOPULATION DE LA FRANCE. \d{3}'
    even_pattern = re.compile(r'DISCUSSION SUR LA DÉPOPULATION DE LA FRANCE. \d{3}')
    even_pattern_matches = even_pattern.findall(text)
    for even_page in even_pattern_matches:
        text = text.replace(even_page, f'[p. {even_page[-3:]}]')
    text = text.replace('-\n', '')
    text = text.replace('\t', ' ')
    return text

raw_text = 'raw_txt/boletim clemence.txt'    
clean_text = 'clean_txt/boletim_clemence.txt'

# call functions
read_save(raw_text, limpar_text, clean_text)
