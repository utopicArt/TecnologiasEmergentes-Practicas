"""
Escribe el código necesario para capturar una cadena de texto y definir una
función para que determinar si es una dirección de correo electrónico valida.
"""
import re

def start():
    email = input('Escriba su direccion de correo: ')
    if validateEmail(email):
        print(f'El correo es correcto')
        requestPassword(email)
    else:
        print("[X]El texto no corresponde a una direccion de correo.")
        start()

def validateEmail(email):
    regex = "^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return re.match(regex, email)

def requestPassword(email):
    password = input('Contraseña: ')
    matchUserPassword(email, password)

def matchUserPassword(email, password):
    print("Do validation stuff...")


if __name__ == '__main__':
    start()
