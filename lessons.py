import datetime, time, webbrowser, os, requests, json
from pathlib import Path
from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser

def loadtext(language):
    with open(f"{Path.home()}\\Documents\\Under the Pebble\\School Connect\\Languages\\{language}.json") as file:
        return json.load(file)

def checkforupdates():
    res = requests.get("https://raw.githubusercontent.com/PodkamykStudio/School-Connect/main/version")
    version = res.text
    dziala = settings["general settings"]["checkforupdates"]
    if dziala == "1":
        if version.strip() != ver.strip():
            window = Tk()
            window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
            window.withdraw()
            if messagebox.askyesno('Update', text["askforupdates"]) == True:
                webbrowser.open(text["askforupdateslink"])
            else:
                pass

def shutdown(godzina1, godzina2):
    czas = datetime.datetime.now().strftime("%H:%M")
    if godzina1 <= czas <= godzina2:
        print(text["askforshutdown"])
        for i in range(1, 31):
            time.sleep(1)
            print("\r", i, end="")

        else:
            print(text["shutdown"])
            os.system("shutdown /s /t 5")

def function(day):
    dziala = settings[day]["active"]
    shutdown_now = settings[day]["shutdown"]
    link = settings[day]["link"]
    godzina1 = settings[day]["time1"]
    godzina2 = settings[day]["time2"]

    if dziala == "1":
        if shutdown_now == "1":
            shutdown(godzina1,godzina2)
        elif godzina1 <= czas <= godzina2:
            if link.strip() == "":
                pass
            else:
                webbrowser.open(link)

    if shutdown_now == "0":
        checkforupdates()

day = datetime.datetime.today().weekday()
czas = datetime.datetime.now().strftime("%H:%M")
days = ["Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
file = open(f"{Path.home()}\\Documents\\Under the Pebble\\School Connect\\version")
settings = ConfigParser()
settings.read(f"{Path.home()}\\Documents\\Under the Pebble\\School Connect\\settings.ini")
text = loadtext(settings["general settings"]["language"])
ver = file.readlines()
ver = ver[0]
file.close()

function(days[day])
