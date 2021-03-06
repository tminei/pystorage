import getpass
import requests
import json
from os import system, name
from datetime import datetime

import wget

indent = 3


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


class short:
    id = {}


def promt():
    promt = input("> ")
    if promt == "exit":
        exit(0)
    elif promt[0:2] == "ls":
        short.id = ls(promt[3:])
    elif promt[0:3] == "pwd":
        pwd()
    elif promt[0:5] == "clear":
        clc()
    elif promt[0:2] == "cd":
        cd(promt[3:])
    elif promt[0:2] == "fs":
        fs()
    elif promt[0:3] == "get":
        getFile(promt[4:])


class path:
    current = "root"


class Longest:
    class Directories:
        name = 4
        viewName = 5
        idName = 2
        permName = 2
        createdAt = 0
        updatedAt = 0

    class Files:
        name = 4
        mime_type = 4
        id = 2
        size = 4
        views = 5
        date = 4


class CurrentLen:
    class Directories:
        name = 0
        viewName = 0
        idName = 0
        permName = 0
        createdAt = 0
        updatedAt = 0

    class Files:
        name = 0
        mime_type = 0
        id = 0
        size = 0
        views = 0
        date = 0


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def pwd():
    if path.current != "root":
        print(bcolors.HEADER + path.current + bcolors.ENDC)
    else:
        print(bcolors.HEADER + "/" + bcolors.ENDC)
    pass


def cd(data):
    params = ""
    if data != "":
        data = data.split(" ")
        try:
            params = "documents?folder_id=" + str(data[0])
        except:
            params = "documents"
        try:
            req = json.loads(get(params, TOKEN).content.decode())
        except:
            print(bcolors.FAIL + "WRONG REQUEST" + bcolors.ENDC)
            return 1
        try:
            if req["status"] == 404:
                print(bcolors.FAIL + "WRONG DIR ID" + bcolors.ENDC)
                return 1
        except:
            pass
        path.current = data[0]

    else:
        path.current = "root"
    pass


def clc():
    clear()


def fs():
    try:
        req = json.loads(get("/folders", TOKEN).content.decode())
    except:
        print(bcolors.FAIL + "WRONG REQUEST" + bcolors.ENDC)
        return 1
    for folder in req:
        try:
            CurrentLen.Directories.name = len(str(folder["name"]))
            CurrentLen.Directories.idName = len(str(folder["id"]))
            CurrentLen.Directories.viewName = len(str(folder["view_count"]))
            CurrentLen.Directories.permName = len(str(folder["permissions"]))
            CurrentLen.Directories.createdAt = len(str(folder["created_at"]))
            CurrentLen.Directories.updatedAt = len(str(folder["updated_at"]))
            if CurrentLen.Directories.name > Longest.Directories.name:
                Longest.Directories.name = CurrentLen.Directories.name
            if CurrentLen.Directories.idName > Longest.Directories.idName:
                Longest.Directories.idName = CurrentLen.Directories.idName
            if CurrentLen.Directories.viewName > Longest.Directories.viewName:
                Longest.Directories.viewName = CurrentLen.Directories.viewName
            if CurrentLen.Directories.permName > Longest.Directories.permName:
                Longest.Directories.permName = CurrentLen.Directories.permName
            if CurrentLen.Directories.createdAt > Longest.Directories.createdAt:
                Longest.Directories.createdAt = CurrentLen.Directories.createdAt
            if CurrentLen.Directories.updatedAt > Longest.Directories.updatedAt:
                Longest.Directories.updatedAt = CurrentLen.Directories.updatedAt
        except:
            continue
    print(bcolors.WARNING + "Name" + bcolors.ENDC, end="")
    for i in range(0, Longest.Directories.name):
        print(" ", end="")
    print(bcolors.WARNING + "ID" + bcolors.ENDC, end="")
    for i in range(-1, Longest.Directories.idName):
        print(" ", end="")
    print(bcolors.WARNING + "Share" + bcolors.ENDC, end="")
    for i in range(0, Longest.Directories.viewName):
        print(" ", end="")
    print(bcolors.WARNING + "Views" + bcolors.ENDC, end="")
    for i in range(0, Longest.Directories.permName):
        print(" ", end="")
    print(bcolors.WARNING + "Perm" + bcolors.ENDC, end="")
    for i in range(0, 7):
        print(" ", end="")
    print(bcolors.WARNING + "created" + bcolors.ENDC, end="")
    for i in range(0, Longest.Directories.updatedAt):
        print(" ", end="")
    print(bcolors.WARNING + "updated" + bcolors.ENDC)

    for folder in req:
        try:
            CurrentLen.Directories.name = len(folder["name"])
            CurrentLen.Directories.idName = len(str(folder["id"]))
            CurrentLen.Directories.viewName = len(str(folder["view_count"]))
            CurrentLen.Directories.permName = len(str(folder["permissions"]))
            CurrentLen.Directories.createdAt = len(str(folder["created_at"]))
            CurrentLen.Directories.updatedAt = len(str(folder["updated_at"]))
            print(bcolors.OKGREEN + folder["name"] + bcolors.ENDC, end="")
            for i in range(-1 - indent, Longest.Directories.name - CurrentLen.Directories.name):
                print(" ", end="")
            print(folder["id"], end="")
            for i in range(0 - indent, Longest.Directories.idName - CurrentLen.Directories.idName):
                print(" ", end="")
            if folder["shared"]:
                print(bcolors.OKGREEN + "  +" + bcolors.ENDC, end='')
            else:
                print(bcolors.FAIL + "  -" + bcolors.ENDC, end='')
            for i in range(0 - indent, Longest.Directories.viewName - CurrentLen.Directories.viewName):
                print(" ", end="")
            print(folder["view_count"], end="")
            for i in range(-5 - indent, Longest.Directories.permName - CurrentLen.Directories.permName):
                print(" ", end="")
            print("   ", end="")
            if folder["permissions"] == "write":
                print(" ", end="")
            print(folder["permissions"][0], end="")
            for i in range(0 - indent, Longest.Directories.createdAt - CurrentLen.Directories.createdAt):
                print(" ", end="")
            print(folder["created_at"], end="")
            for i in range(0 - indent, Longest.Directories.updatedAt - CurrentLen.Directories.updatedAt):
                print(" ", end="")
            print(folder["updated_at"])
        except:
            continue


def ls(data):
    shortID = {}
    pwd()
    params = ""
    if data != "":
        data = data.split(" ")
        if data[0] == "/":
            try:
                params = "documents"
            except:
                params = ""
        else:
            try:
                params = "documents?folder_id=" + str(data[0])
            except:
                params = ""
    else:
        if path.current != "root":
            params = "documents?folder_id=" + path.current
        else:
            params = "documents"

    try:
        req = json.loads(get(params, TOKEN).content.decode())
    except:
        print(bcolors.FAIL + "WRONG REQUEST" + bcolors.ENDC)
        return 1
    folders = []
    files = []
    try:
        for i in req["entries"]:
            try:
                if i["folder"]:
                    folders.append(i)
            except:
                pass
            try:
                if i["@type"] == 'message':
                    files.append(i)
            except:
                pass

        if len(folders) > 0:
            print(bcolors.FAIL + "DIRECTORIES" + bcolors.ENDC)
            for folder in folders:
                CurrentLen.Directories.name = len(str(folder["name"]))
                CurrentLen.Directories.idName = len(str(folder["id"]))
                CurrentLen.Directories.viewName = len(str(folder["view_count"]))
                CurrentLen.Directories.permName = len(str(folder["permissions"]))
                if CurrentLen.Directories.name > Longest.Directories.name:
                    Longest.Directories.name = CurrentLen.Directories.name
                if CurrentLen.Directories.idName > Longest.Directories.idName:
                    Longest.Directories.idName = CurrentLen.Directories.idName
                if CurrentLen.Directories.viewName > Longest.Directories.viewName:
                    Longest.Directories.viewName = CurrentLen.Directories.viewName
                if CurrentLen.Directories.permName > Longest.Directories.permName:
                    Longest.Directories.permName = CurrentLen.Directories.permName
            print(bcolors.WARNING + "Name" + bcolors.ENDC, end="")
            for i in range(0, Longest.Directories.name):
                print(" ", end="")
            print(bcolors.WARNING + "ID" + bcolors.ENDC, end="")
            for i in range(-1, Longest.Directories.idName):
                print(" ", end="")
            print(bcolors.WARNING + "Share" + bcolors.ENDC, end="")
            for i in range(0, Longest.Directories.viewName):
                print(" ", end="")
            print(bcolors.WARNING + "Views" + bcolors.ENDC, end="")
            for i in range(0, Longest.Directories.permName):
                print(" ", end="")
            print(bcolors.WARNING + "Perm" + bcolors.ENDC)

            for folder in folders:
                CurrentLen.Directories.name = len(folder["name"])
                CurrentLen.Directories.idName = len(str(folder["id"]))
                CurrentLen.Directories.viewName = len(str(folder["view_count"]))
                CurrentLen.Directories.permName = len(str(folder["permissions"]))
                print(bcolors.OKGREEN + folder["name"] + bcolors.ENDC, end="")
                for i in range(-1 - indent, Longest.Directories.name - CurrentLen.Directories.name):
                    print(" ", end="")
                print(folder["id"], end="")
                for i in range(0 - indent, Longest.Directories.idName - CurrentLen.Directories.idName):
                    print(" ", end="")
                if folder["shared"]:
                    print(bcolors.OKGREEN + "  +" + bcolors.ENDC, end='')
                else:
                    print(bcolors.FAIL + "  -" + bcolors.ENDC, end='')
                for i in range(0 - indent, Longest.Directories.viewName - CurrentLen.Directories.viewName):
                    print(" ", end="")
                print(folder["view_count"], end="")
                for i in range(-5 - indent, Longest.Directories.permName - CurrentLen.Directories.permName):
                    print(" ", end="")
                if folder["permissions"] == "write":
                    print(" ", end="")
                print(folder["permissions"])
            print()

        if len(files) > 0:
            print(bcolors.FAIL + "FILES" + bcolors.ENDC)
            for file in files:
                shortID.update({str(file["content"]["document"]["document"]["id"]): str(file["id"])})
                human_size = file["content"]["document"]["document"]["size"]
                human_size_type = "B"
                if human_size > 1024:
                    human_size = human_size / 1024
                    human_size_type = "KB"
                    if human_size > 1024:
                        human_size = human_size / 1024
                        human_size_type = "MB"
                        if human_size > 1024:
                            human_size = human_size / 1024
                            human_size_type = "GB"
                human_size = round(human_size, 2)
                human_size = str(str(human_size) + " " + human_size_type)
                human_date = (datetime.utcfromtimestamp(file["date"]).strftime('%Y-%m-%d %H:%M:%S'))
                CurrentLen.Files.date = len(str(human_date))
                CurrentLen.Files.size = len(human_size)
                CurrentLen.Files.name = len(str(file["content"]["document"]["file_name"]))
                CurrentLen.Files.mime_type = len(str(file["content"]["document"]["mime_type"]))
                CurrentLen.Files.id = len(str(file["content"]["document"]["document"]["id"]))
                CurrentLen.Files.views = len(str(file["views"]))

                if CurrentLen.Files.name > Longest.Files.name:
                    Longest.Files.name = CurrentLen.Files.name
                if CurrentLen.Files.mime_type > Longest.Files.mime_type:
                    Longest.Files.mime_type = CurrentLen.Files.mime_type
                if CurrentLen.Files.id > Longest.Files.id:
                    Longest.Files.id = CurrentLen.Files.id
                if CurrentLen.Files.size > Longest.Files.size:
                    Longest.Files.size = CurrentLen.Files.size
                if CurrentLen.Files.views > Longest.Files.views:
                    Longest.Files.views = CurrentLen.Files.views
                if CurrentLen.Files.date > Longest.Files.date:
                    Longest.Files.date = CurrentLen.Files.date

            print(bcolors.WARNING + "Name" + bcolors.ENDC, end="")
            for i in range(0, Longest.Files.name):
                print(" ", end="")
            print(bcolors.WARNING + "Type" + bcolors.ENDC, end="")
            for i in range(-1, Longest.Files.mime_type):
                print(" ", end="")
            print(bcolors.WARNING + "ID" + bcolors.ENDC, end="")
            for i in range(0, Longest.Files.id):
                print(" ", end="")
            print(bcolors.WARNING + "Size" + bcolors.ENDC, end="")
            for i in range(0, Longest.Files.size):
                print(" ", end="")
            print(bcolors.WARNING + "Views" + bcolors.ENDC, end="")
            for i in range(0, Longest.Files.views):
                print(" ", end="")
            print(bcolors.WARNING + "Date" + bcolors.ENDC)

            for file in files:
                human_size = file["content"]["document"]["document"]["size"]
                human_size_type = "B"
                if human_size > 1024:
                    human_size = human_size / 1024
                    human_size_type = "KB"
                    if human_size > 1024:
                        human_size = human_size / 1024
                        human_size_type = "MB"
                        if human_size > 1024:
                            human_size = human_size / 1024
                            human_size_type = "GB"
                human_size = round(human_size, 2)
                human_size = str(str(human_size) + " " + human_size_type)
                human_date = (datetime.utcfromtimestamp(file["date"]).strftime('%Y-%m-%d %H:%M:%S'))
                CurrentLen.Files.date = len(str(human_date))
                CurrentLen.Files.size = len(human_size)
                CurrentLen.Files.name = len(str(file["content"]["document"]["file_name"]))
                CurrentLen.Files.mime_type = len(str(file["content"]["document"]["mime_type"]))
                CurrentLen.Files.id = len(str(file["content"]["document"]["document"]["id"]))
                CurrentLen.Files.views = len(str(file["views"]))
                print(bcolors.OKBLUE + file["content"]["document"]["file_name"] + bcolors.ENDC, end="")
                for i in range(-1 - indent, Longest.Files.name - CurrentLen.Files.name):
                    print(" ", end="")
                print(file["content"]["document"]["mime_type"], end="")
                for i in range(-2 - indent, Longest.Files.mime_type - CurrentLen.Files.mime_type):
                    print(" ", end="")
                print(file["content"]["document"]["document"]["id"], end="")
                for i in range(1 - indent, Longest.Files.id - CurrentLen.Files.id):
                    print(" ", end="")
                print(human_size, end="")
                for i in range(-1 - indent, Longest.Files.size - CurrentLen.Files.size):
                    print(" ", end="")
                print(file["views"], end="")
                for i in range(-2 - indent, Longest.Files.views - CurrentLen.Files.views):
                    print(" ", end="")
                print(human_date)
        return shortID
    except:
        print(bcolors.FAIL + "Invalid folder id!" + bcolors.ENDC)
        return 1


def getFile(data):
    try:
        id = short.id[str(data)]
    except:
        pass
    try:
        # req = get("of/" + str(id), TOKEN)
        req = json.loads(get("of/" + str(id), TOKEN).content.decode())
        print(req)
    except:

        pass
    try:

        wget.download(req["l"], req["name"])
        print()
    except:
        pass


def get(adr, TOKEN):
    try:
        req = requests.get('https://www.xran.ru/' + adr,
                           headers={'Accept': 'application/json',
                                    'Authorization': TOKEN}, )
    except:
        return 1
    return req


if __name__ == '__main__':

    while True:
        login_data = getpass.getpass("Please enter you login@password from xran.ru or type 'exit' to exit:\n")
        if login_data == "exit":
            exit(0)
        try:
            login_data = login_data.split("@")
            auth_data = {'login': login_data[0], 'password': login_data[1]}
        except:
            continue
        break
    session = requests.Session()
    auth = session.post('https://www.xran.ru/users/telegram/authorize', {
        'username': auth_data['login'],
        'password': auth_data['password'],
        'remember': 1,
    })
    try:
        TOKEN = eval(auth.content.decode())["access_token"]
    except:
        print("Wrong login data!")
        exit(1)

    clear()
    print("You logged in.")
    while True:
        promt()
