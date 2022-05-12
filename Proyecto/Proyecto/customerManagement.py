from utils import add_class, remove_class
from js import document, console
import json
import os

out = document.getElementById("out")
out.innerHTML += "<p>⏳Cargando el código python...</p>"

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
    out.innerHTML += f"<p>Se obtuvo: {data}</p>"    
    return data

def getData():
    out.innerHTML += "<p>Obteniendo datos...</p>"
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
    out.innerHTML += f"<p>✔️Cliente creado: {userData}</p>"


def create_contact(*ags, **kws):
    out.innerHTML += "<p>Verificando archivo...</p>"
    #createNewFile()
    #out.innerHTML += "<p>Obteniendo entrada del usuario...</p>"
    #getData()

out.innerHTML += "✔️Cargado" 