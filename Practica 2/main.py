"""
Escribe el código necesario para capturar una cadena de texto.
1.- Escribe una función que verdadero o falso si la primera letra de la cadena de
texto es mayúscula.
2.- Escribe una función que cuente las palabras que forman la cadena de texto.
3.- Escribe una función que reciba como argumento la cadena de texto y regrese
una lista con las palabras que la forman.
4.- Escribe una función que regrese la cadena de texto invertida.
5.- Escribe una función que regrese la cadena original con la última letra de cada
palabra en mayúscula.

"""

def isUpperCase(text):
    if text[0].isupper():
        return True
    return False

def countWords(text):
    counter = len(text.split())
    return counter

def getWordsInText(text):
    words = text.split(" ")
    return words

def reverseString(text):
    return text[::-1]

def setUpperCaseLetter(text):
    word = getWordsInText(text)
    words = []
    for i in range(len(word)):
        words.append(word[i][:-1] + word[i][-1].upper())
    text = format(' '.join(words))

    return text

def main():
    text = input('Escriba el texto: ')
    print(f"La primer letra {'es' if isUpperCase(text) else 'no es'} mayuscula.")

    print(f'Hay {countWords(text)} palabras')

    print(f'La cadena esta conformada por las siguietes palabra {getWordsInText(text)}')

    print(f'Cadena invertida: {reverseString(text)}')

    print(f'Ultima letra de cada palabra en mayúscula: {setUpperCaseLetter(text)}')

if __name__ == '__main__':
    main()

