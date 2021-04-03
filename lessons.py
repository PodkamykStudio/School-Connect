import datetime, time, webbrowser, os
from pathlib import Path

def shutdown(godzina1, godzina2):
    czas = datetime.datetime.now().strftime("%H:%M")
    if godzina1 <= czas <= godzina2:
        print("Masz 30 sekund aby zamknąć to okno inaczej komputer się wyłączy")
        for i in range(1, 31):
            time.sleep(1)
            print("\r", i, end="")

        else:
            print("Zaraz nastąpi wyłączenie systemu")
            os.system("shutdown /s /t 5")

def function(link):
    if dziala == "1":
        if shutdown_now == "1":
            shutdown(godzina1,godzina2)
        elif godzina1 <= czas <= godzina2:
            webbrowser.open(link)

day = datetime.datetime.today().weekday()
czas = datetime.datetime.now().strftime("%H:%M")
file = open(f"{Path.home()}\\Documents\\Under the Pebble\\School Connect\\settings.txt")
settings = file.readlines()
file.close()


if day == 0:
    dziala = settings[4].strip()
    shutdown_now = settings[6].strip()
    link1 = settings[8]
    godzina1 = settings[10]
    godzina2 = settings[12]

    function(link1)

if day == 1:
    dziala = settings[16].strip()
    shutdown_now = settings[18].strip()
    link2 = settings[20]
    godzina1 = settings[22]
    godzina2 = settings[24]

    function(link2)

if day == 2:
    dziala = settings[28].strip()
    shutdown_now = settings[30].strip()
    link3 = settings[32]
    godzina1 = settings[34]
    godzina2 = settings[36]

    function(link3)

if day == 3:
    dziala = settings[40].strip()
    shutdown_now = settings[42].strip()
    link4 = settings[44]
    godzina1 = settings[46]
    godzina2 = settings[48]

    function(link4)

if day == 4:
    dziala = settings[52].strip()
    shutdown_now = settings[54].strip()
    link5 = settings[56]
    godzina1 = settings[58]
    godzina2 = settings[60]

    function(link5)

if day == 5:
    dziala = settings[64].strip()
    shutdown_now = settings[66].strip()
    link6 = settings[68]
    godzina1 = settings[70]
    godzina2 = settings[72]

    function(link6)

if day == 6:
    dziala = settings[76].strip()
    shutdown_now = settings[78].strip()
    link7 = settings[80]
    godzina1 = settings[82]
    godzina2 = settings[84]

    function(link7)
    
