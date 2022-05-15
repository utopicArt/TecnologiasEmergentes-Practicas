from utils import add_class, remove_class
from js import document, console
import json
import os

out = document.getElementById("out")
out.innerHTML += "⏳Loading Python code..."
isLoaded = False

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
    out.innerHTML += f"\\\n✔️Client created successfully: {userData}"

def getDetails(user):
    out.innerHTML += f"\\\n👉Customer selected: {user}"


def create_contact(*ags, **kws):
    out.innerHTML += "\\\n🛈 Verificando archivo de base de datos...\\\n"
    #createNewFile()
    #out.innerHTML += "<p>Obteniendo entrada del usuario...</p>"
    #setData()

def getContactsName():
    ul = document.getElementById('myUL')
    with open('data.json') as file:
        data = json.load(file)
        counter = 0
        for clients in data['customer']:
            for client in clients['client']:
                contact = client['Contact_Information']
                name = f'{contact["first_name"]} {contact["last_name"]}'
                out.innerHTML += '\\\nContact found: ' + name
                ul.innerHTML += f"""
                <li id='element'>                
                    <py-button id='data{counter}' label='{name}' title='{name}'>
                        def on_click(evt):
                            getDetails('{name}')             
                    </py-button>
                </li>"""
                counter += 1

out.innerHTML += "\\\n✔️Python Loaded." 
out.innerHTML += "\\\n📁Getting contacts..." 
getContactsName()