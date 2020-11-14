'''
Build a Translator in Python
Author: Ayushi Rawat
'''

#import the package
from googletrans import Translator
from googletrans.gtoken import TokenAcquirer

# Store some text for translation:
textoOriginal = input('Insira o texto a ser traduzido: ')

tLang = input('Defina o idioma da tradução final: ')
# Create an instance of Translator to use
translator = Translator()

# detect the language
lang = translator.detect(textoOriginal)
print(f'Idioma original: {lang}')

# Call the translate()
textoTraduzido = translator.translate(textoOriginal, dest=f'{tLang}')

#print the result
print(f'Tradução para o {tLang}: {textoTraduzido.text}')

#translated = translator.translate(text, dest = 'pt')

#print(translated.text)
