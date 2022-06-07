"""Script to clean text from a file.
"""
import re

# function to clean text
def limpar_text(text, odd, even):
    """Clean text.
    """
    # find matches for the odd pattern (check if the doc pages are 2 or 3 digits long)
    odd_pattern = re.compile(odd + r' \d{3}')
    odd_pattern_matches = odd_pattern.findall(text)
    for odd_page in odd_pattern_matches:
        text = text.replace(odd_page, f'[p. {odd_page[-3:]}]')
    # find matches for the even pattern 
    even_pattern = re.compile(r'\d{3} '+ even)
    even_pattern_matches = even_pattern.findall(text)
    for even_page in even_pattern_matches:
        text = text.replace(even_page, f'[p. {even_page[0:3]}]')
    text = text.replace('-\n', '')
    text = text.replace('\t', ' ')
    return text

#function to save text in a file
def save_text(text, filename):
    """Save text in a file.
    """
    with open(filename, 'w') as file:
        file.write(text)

# read file
def read_save(raw_text, clean_function, odd, even, clean_text):
    with open(raw_text, 'r') as f:
        text = f.read()
        #call function
        print('Cleaning text...')
        text = clean_function(text, odd, even,)
        #save result
        save_text(text, clean_text)


# pass path to raw text and clean text
raw_text =  input('Enter path to raw text: ')
clean_text = input('Enter path to clean text: ')

#pass odd and even patterns
odd = input('Enter odd pattern: ')
even = input('Enter even pattern: ')

# call functions
read_save(raw_text, limpar_text, odd, even, clean_text)
