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

newFile = False
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
    userData['client'] = []

    userData['client'].append({
            'Contact_Information': {
                'first_name': basicInformation(),
                'last_name1': input("Apellido Paterno: "),
                'last_name2': input("Apellido Materno: "),
                'birthDay' : input("Dia de nacimiento: "),
                'birthMonth': input("Mes de nacimiento: "),
                'birthYear': input("Año de nacimiento: "),
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
        })

    with open('data.json', 'r+') as file:
        #json.dump(userData, file, indent=4)
        fileData = json.load(file)
        fileData["customer"].append(userData)
        file.seek(0)
        json.dump(fileData, file, indent=4)

    main()

def showInformation():
    #Obtener los datos
    with open('data.json') as file:
        data = json.load(file)
        for clients in data['customer']:
            for client in clients['client']:
                print(f"Response = {client['Contact_Information']['first_name']}")
                contact = client['Contact_Information']
                job = client['Job_Information']
                billing = client['Billing_Information']

                name = f'{contact["first_name"]} {contact["last_name1"]} {contact["last_name2"]}'

                birthday = f'{contact["birthDay"]}-{contact["birthMonth"]}-{contact["birthYear"]}'

                print(f'Nombre: {name}')
                print(f'Fecha de nacimiento: {birthday}')

                print(f'Telefono: {contact["phone"]}')
                print(f'Correo: {contact["email"]}')

                print(f'Empresa: {job["company"]}')
                print(f'Cargo: {job["title"]}')

                print(f'Calle de residencia: {billing["street"]}')
                print(f'Numero Exterior: {billing["houseExt"]}')
                print(f'Numero Interior: {billing["houseInt"]}')
                print(f'Colonia: {billing["suburb"]}')
                print(f'Ciudad: {billing["city"]}')
                print(f'Estado: {billing["state"]}')
                print(f'Codigo postal: {billing["postalCode"]}')



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

def createNewFile():
    newFile = False
    try:
        file = open("data.json", "a+")
        if os.stat("data.json").st_size == 0:
            file.write('{\n\t"customer": []\n}')
            file.close()
    except:
        newFile = True
        print("Trono")


if __name__ == '__main__':
    createNewFile()
    main()
    #showInformation()
