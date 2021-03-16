import datetime, time, webbrowser, os, getpass
from pathlib import Path

user = getpass.getuser()
day = datetime.datetime.today().weekday()
czas = datetime.datetime.now().strftime("%H:%M")
file = open(f"{Path.home()}\\Documents\\Under the Pebble\\School Connect\\settings.txt")
settings = file.readlines()
file.close()

print(settings)
if day == 0:
    link1 = settings[4]
    godzina1 = settings[6]
    godzina2 = settings[8]

    if godzina1 <= czas <= godzina2:
        webbrowser.open(link1)

if day == 1:
    link2 = settings[12]
    godzina1 = settings[14]
    godzina2 = settings[16]

    if godzina1 <= czas <= godzina2:
        webbrowser.open(link2)

if day == 2:
    link3 = settings[20]
    godzina1 = settings[22]
    godzina2 = settings[24]

    if godzina1 <= czas <= godzina2:
        webbrowser.open(link3)

if day == 3:
    link4 = settings[28]
    godzina1 = settings[30]
    godzina2 = settings[32]

    if godzina1 <= czas <= godzina2:
        webbrowser.open(link4)

if day == 4:
    link5 = settings[36]
    godzina1 = settings[38]
    godzina2 = settings[40]

    if godzina1 <= czas <= godzina2:
        webbrowser.open(link5)

if day == 5 or day == 6:

    if "08:50" <= czas <= "09:00":
        print("Masz 30 sekund aby zamknąć to okno inaczej komputer się wyłączy")
        for i in range(1, 31):
            time.sleep(1)
            print("\r", i, end="")

        else:
            print("Zaraz nastąpi wyłączenie systemu")
            os.system("shutdown /s /t 5")