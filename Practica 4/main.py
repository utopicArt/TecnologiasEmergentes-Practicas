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
    cls()
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

    userData['customer'].append({
        'client': {
            'Contact_Information': {
                'first_name': basicInformation(),
                'last_name1': input("Apellido Paterno: "),
                'last_name2': input("Apellido Materno: "),
                'birthDay' : input("Dia de nacimiento: "),
                'birthMonth': input("Mes de nacimiento: "),
                'birthYear': int(input("Año de nacimiento: ")),
                'phone': input("Telefono:\t\t\t"),
                'email': input("Correo:\t\t\t  ")
            },
            'Job_Information': {
                'company': jobInformation(),
                'title': input("Cargo:\t\t")
            },
            'Billing_Information': {
                'street': billingInformation(),
                'houseExt': input("Numero exterior: "),
                'houseInt': input("Numero interior: "),
                'suburb': input("Colonia:\t\t "),
                'city': input("Municipio:\t\t "),
                'state': input("Estado:\t\t\t "),
                'postalCode': input("Codigo postal:\t ")
            }
        }
    })
    with open('data.json', 'w') as file:
        json.dump(userData, file, indent=4)
    main()

def showInformation():
    #Obtener los datos
    with open('data.json') as file:
        data = json.load(file)
        for client in data['customer']:
            print(client)
            contact = client['client']['Contact_Information']
            print(f'Nombre: {contact["first_name"]}')
            print(f'Apellido Paterno: {contact["last_name1"]}')
            print(f'Apellido Materno: {contact["last_name2"]}')
            print(f'Fecha de nacimiento: {contact["birthDay"]}-{contact["birthMonth"]}-{contact["birthYear"]}')
            print(f'Telefono: {contact["phone"]}')
            print(f'Correo: {contact["email"]}')

def showTemplate():
    #Mostrar la base - dejar al final
    print("showTemplate")

def basicInformation():
    print(f"{'*' * 37}\n*\tInformacion de Contacto\t\t\t*\n{'*' * 37}")
    return input("Nombre:\t\t\t  ")

def jobInformation():
    cls()
    print(f"{'*' * 37}\n*\tInformacion de Trabajo\t\t\t*\n{'*' * 37}")
    return input("Empresa:\t")

def billingInformation():
    cls()
    print(f"{'*' * 37}\n*\t\t\tDomicilio\t\t\t\t*\n{'*' * 37}")
    return input("Calle:\t\t\t ")


if __name__ == '__main__':
    #main()
    showInformation()

