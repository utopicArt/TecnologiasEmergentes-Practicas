"""
En un archivo de texto plano registra información de personas (nombre,
apellido1, apellido2, cargo, empresa, calle, numeroExt, numeroInt, colonia,
municipio, estado, codigoPostal, telefono, correoElectronico,
fechaNacimiento, edad calculada), el formato lo determinarás de acuerdo a
la implementación.

En otro archivo de texto plano elabora un “oficio”, con la estructura que
consideres necesaria para incluir la información de las personas (archivo
anterior).

Elabora un programa en Python que cree un oficio por cada registro de
personas y que reemplace los datos de las mismas en el texto del oficio.
"""

from datetime import date
import os
import json

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    optionSelected = int(input("""
    ======Sistema de manejo de clientes======
    
    1.- Ingresar informacion
    2.- Mostrar informacion
    3.- Mostrar template de oficio
    
    Opcion: """))
    cls()

    if optionSelected == 1:
        createTemplate()
    elif optionSelected == 2:
        showInformation()
    elif optionSelected == 3:
        showTemplate()
    else:
        main()



def createTemplate():
    userData = {}
    userData['customer'] = []

    print(f"{'*'*37}\n*\tInformacion de Contacto\t\t\t*\n{'*'*37}")
    name = input("Nombre:\t\t")
    lastName = input("Apellidos:\t")
    lastName = lastName.split(' ')
    dateBirth = input("Fecha de nacimiento (dd/mm/yyyy): ")
    dateBirth = dateBirth.split('/')
    #ageCalculated = date.today().year - dateBirth
    phone = input("Telefono:\t")
    email = input("Correo electronico: ")
    cls()
    print(f"{'*' * 37}\n*\tInformacion de Empresa\t\t\t*\n{'*' * 37}")
    company = input("Empresa:\t")
    title = input("Cargo:\t\t")
    cls()
    print(f"{'*' * 37}\n*\t\t\tDomicilio\t\t\t\t*\n{'*' * 37}")
    street = input("Calle:\t\t\t ")
    houseExt = input("Numero exterior: ")
    houseInt = input("Numero interior: ")
    suburb = input("Colonia:\t\t ")
    town = input("Municipio:\t\t ")
    state = input("Estado:\t\t\t ")
    postalCode =input("Codigo postal:\t ")

    userData['customer'].append({})
def saveDataFile():
    filename = './bases/default.json'
    files = [('JSON File', '*.json')]
    base = {}
    with open(filename, 'w') as outfile:
        json.dump(base, outfile)

def showInformation():
    #Obtener los datos
    print("showInformation")

def showTemplate():
    #Mostrar la base - dejar al final
    print("showTemplate")


if __name__ == '__main__':
    #main()
    data = {}
    data['customer'] = []
    data['customer'].append({
        'client': {
        'basic_information' : {
            'first_name': input("Nombre:\t\t"),
            'last_name': input("Apellidos:\t"),
            'age': input("Edad: "),
        },
        'financial_information' : {
            'amount': input("Enter an amount: ")
        }}})
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

