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
    odd_pages = [odd_page.replace('SÉANCE DU 2 OCTOBRE 1890.', '') for odd_page in odd_pattern_matches]
    for odd_page in odd_pages:
        odd_page = odd_page.strip()
        text = text.replace(odd_page, f'[p. {odd_page}]')
    text = text.replace(' SÉANCE DU 2 OCTOBRE 1890.', '')
    # find matches for the pattern 'DISCUSSION SUR LA DÉPOPULATION DE LA FRANCE. \d{3}'
    even_pattern = re.compile(r'DISCUSSION SUR LA DÉPOPULATION DE LA FRANCE. \d{3}')
    even_pattern_matches = even_pattern.findall(text)
    even_pages = [even_page.replace('DISCUSSION SUR LA DÉPOPULATION DE LA FRANCE. ', '') for even_page in even_pattern_matches]
    for even_page in even_pages:
        text = text.replace(even_page, f'[p. {even_page}]')
    text = text.replace('DISCUSSION SUR LA DÉPOPULATION DE LA FRANCE. ', '')
    text = text.replace('-\n', '')
    # find pattern \n, strings and remove \n 
    text = text.replace('\t', ' ')
    return text

raw_text = 'raw_txt/boletim clemence.txt'    
clean_text = 'clean_txt/boletim_clemence.txt'

# call functions
read_save(raw_text, limpar_text, clean_text)
