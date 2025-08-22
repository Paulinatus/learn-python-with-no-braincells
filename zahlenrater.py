import random 
import time
gesuchte = random.randint(0,100)
print(gesuchte)
print("Guten morgen.")
print("Ich habe mir eine zufällige zahl ausgedacht.")
print("Versuche doch sie zu erraten")
geraten=0
while geraten!=gesuchte:
    geraten=int(input())
    if geraten==gesuchte:
        print("Glückwunsch das ist die richtige Zahl.")
        print("Auf Wiedersehen")
        time.sleep(5)
        break
    else:
        if geraten > gesuchte:
            print("Diese Zahl ist leider Falsch")
            print("Die gesuchte Zahl ist kleiner")
        else:
            print("Diese Zahl ist leider Falsch.")
            print("Die gesuchte Zahl ist größer")