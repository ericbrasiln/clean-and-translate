"""Script to clean text from a file.
"""
import re
from aux_functions import *

# function to clean text
def limpar_text(text):
    """Clean text.
    """
    # find matches for the pattern \n, string and \n
    head_pattern = re.compile(r'\nRevue d\'Histoire des Sciences Humaines\s+')
    # find all matches
    heads = head_pattern.findall(text)
    for head in heads:
        text = text.replace(head, '')
    # find pattern \n, string and \n
    author_pattern = re.compile(r'\nJean-Claude Wartelle\s+')
    # find all matches
    authors = author_pattern.findall(text)
    for author in authors:
        text = text.replace(author, '')
    # find pattern \n, string and \n
    page_pattern = re.compile(r'\n\d{3}\n')
    # find all matches
    pages = page_pattern.findall(text)
    for page in pages:
        text = text.replace(page, f'[p. {page}]')
    # replace [p. \n\d{2}\n] with [p. \d{3}]
    clean_page_pattern = re.compile(r'\[p\.\s+\d{3}\n\]')
    clean_pages = clean_page_pattern.findall(text)
    for clean_page in clean_pages:
        text = text.replace(clean_page, f'\n[p.{clean_page[5:8]}]\n')
    text = text.replace('-\n', '')
    text = text.replace('\n\n', '\n')
    text = text.replace('\t', ' ')
    return text

raw_text = 'raw_txt/clémence_Soc_Antrop_Paris.txt'
clean_text = 'clean_txt/soc_antrop_paris.txt'

# call functions
read_save(raw_text, limpar_text, clean_text)
