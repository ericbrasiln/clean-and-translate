'''Translater using deep-translator
'''
from deep_translator import (GoogleTranslator)

# function to split text into pages
def split_text(text):
    '''Split text by pattern \n\[p\.\s\d+\]\s+'''
    with open(text, 'r') as f:
        text = f.read()
        #text_list = text.split('[p. ') #pattern to 'boletim_clemence.txt
        text_list = text.split('[p.') #pattern to 'lecture_de_darwin.txt and soc_antrop_paris.txt
    return text_list

# function to save the translated text to a file
def save_translated_text(translated_text, filename):
    '''Save the translated text to a file
    '''
    with open(filename, 'w') as f:
        f.write(translated_text)

# function to translate text
def translate_text(source_file, source_language, target_language):
    '''Translate text
    '''
    translated_text = GoogleTranslator(source=source_language, target=target_language).translate(text=source_file)
    return translated_text

source_file = input(str('Enter the source file name: '))
source_language = input(str('Enter the source language: '))
target_language = input(str('Enter the target language: '))
translated_file = input(str('Enter the translated file name: '))

# call function to split text into pages
pages = split_text(source_file)
print('Number of pages: ', len(pages))
print('Translating...')
# empty list to store translated text
translated_list = []
for page in pages:
    # remove \n
    page = page.replace('\n', '')
    # callfunction to translate text
    translated_text = translate_text(page, source_language, target_language)
    # add translated text to list
    translated_list.append(translated_text)
# join translated text
final_translation = '\n'.join(translated_list)
save_translated_text(final_translation, translated_file)
