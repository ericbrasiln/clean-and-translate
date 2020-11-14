#Importando o pacote
from googletrans import Translator

# Inserindo o texto a ser traduzido
textoOriginal = input('Insira o texto a ser traduzido: ')

# Definindo o idioma para tradução
tLang = input('Defina o idioma da tradução final: ')

# Criando a intância do Translator para uso
translator = Translator()

# Detectando o idioma do texto original
lang = translator.detect(textoOriginal)
print(f'Idioma original: {lang}')

# Chamando o translate(), definindo tb a língua da tradução
textoTraduzido = translator.translate(textoOriginal, dest=f'{tLang}')

# Imprimindo o resultado na tela
print(f'Tradução para o {tLang}: {textoTraduzido.text}')
