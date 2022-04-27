
"""
Escribe el código necesario para capturar una cadena de texto y definir una
función para que determinar si es una dirección de correo electrónico valida.
"""
from getpass import getpass


def start():
    email = input('Escriba su direccion de correo: ')
    if validateEmail(email):
        requestPassword(email)
    else:
        print("[X]El texto no corresponde a una direccion de correo.")
        start()

def validateEmail(email):
    print("validate")

def requestPassword(email):
    print("some")
    password = getpass('Contraseña: ')
    matchUserPassword(email, password)

def matchUserPassword(email, password):
    print("Do validation stuff...")



if __name__ == '__main__':
    #start()
    requestPassword("text@mail.com")


