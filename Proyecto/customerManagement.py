from utils import add_class, remove_class
from js import document, console
import json
import os

out = document.getElementById("out")
out.innerHTML += "⏳Cargando el código python..."

def createNewFile():
    newFile = False
    try:
        file = open("data.json", "a+")
        if os.stat("data.json").st_size == 0:
            file.write('{\n\t"customer": []\n}')
            file.close()
    except:
        newFile = True
        out.innerHTML += "❌Fail to create file"

def getInputData(id):
    data = document.getElementById(id).value
    out.innerHTML += f"\\\nSe obtuvo: {data}\\\n"    
    return data

def setData():
    out.innerHTML += "\\\nObteniendo datos...\\\n"
    userData = {}
    userData['client'] = []
    userData['client'].append({
            'Contact_Information': {
                'first_name': getInputData("first_name"),
                'last_name': getInputData("last_name"),
                'birthday' : getInputData("birthday"),
                'phone': getInputData("phone"),
                'email': getInputData("email"),
            },
            'Job_Information': {
                'company': getInputData("company"),
                'title': getInputData("title")
            },
            'Billing_Information': {
                'country': getInputData("country"),
                'state': getInputData("state"),
                'city': getInputData("city"),
                'street': getInputData("street"),
                'houseExt': getInputData("houseExt"),
                'houseInt': getInputData("houseInt"),
                'suburb': getInputData("suburb"),
                'postalCode': getInputData("postalCode")
            }
        })
    #with open('data.json', 'r+') as file:
    #    #json.dump(userData, file, indent=4)
    #    fileData = json.load(file)
    #    fileData["customer"].append(userData)
    #    file.seek(0)
    #    json.dump(fileData, file, indent=4)        
    out.innerHTML += f"\\\n✔️Cliente creado: {userData}"

def on_click(user):
    console.log(f"\\\n✔️Cliente seleccionado: {user}")


def create_contact(*ags, **kws):
    out.innerHTML += "\\\n🛈 Verificando archivo de base de datos...\\\n"
    #createNewFile()
    #out.innerHTML += "<p>Obteniendo entrada del usuario...</p>"
    #setData()

out.innerHTML += "\\\n✔️Cargado" 