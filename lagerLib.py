from json import dumps, loads
from string import ascii_letters, digits
from random import choice

productStorageConfigPath = ""
productLibraryConfigPath = ""
storageData = {}
libraryData = {}


def printConfig():
    print(storageData)

def newID32():
    return "".join([str(choice(ascii_letters+digits)) for _ in range(32)])



def newProduct(uuid:str, name:str, charge:int, typ:int)->dict:
    return {
        "uuid":uuid,
        "name": name,
        "charge": charge,
        "typ": typ
    }

def newWafer(uuid:str, name:str, charge:int, typ:int, sperrVermerk:bool, reserviert:str)->dict:
    return {
        "uuid":uuid,
        "name": name,
        "charge": charge,
        "typ": typ,
        "sperr_vermerk": sperrVermerk,
        "reserviert": reserviert
    }

def addEntry(id_:str, contentData:dict): # format "<int>:<str>"
    #print(contentData)
    if id_ in storageData.keys():
        storageData[id_].append(contentData["uuid"])

    else:
        storageData[id_] = [contentData["uuid"]]
    libraryData[contentData["uuid"]] = contentData




def delEntry(uuid:str):
    for key, value_list in storageData.items():
        if uuid in value_list:
            value_list.remove(uuid)



def writeConfigStorage():
    file = open(productStorageConfigPath, "w")
    file.write(dumps(storageData, indent=4))
    file.close()
def writeConfigLibary():
    file = open(productLibraryConfigPath, "w")
    file.write(dumps(libraryData, indent=4))
    file.close()

def readConfigStorage()->dict:
    global storageData
    file = open(productStorageConfigPath, "r")
    content = file.read()
    file.close()
    storageData = loads(content)
    return storageData

def readConfigLibrary()->dict:
    global libraryData
    file = open(productLibraryConfigPath, "r")
    content = file.read()
    file.close()
    libraryData = loads(content)
    return libraryData


def waitForScan():
    pass

def newWaferFromData(uuid:str):
    return libraryData[uuid]


