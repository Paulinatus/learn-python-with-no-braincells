import time
i="y"
while i=="y":
    print("please choose one option for calculation")
    print("1=+")
    print("2=-")
    print("3=*")
    print("4=:")
    zahl1=int(0) 
    zahl2=int(0)
    rechenart=int(input())
    if rechenart == 1:
        print("Whats your first number?")
        zahl1=int(input())
        print("Whats your second number?")
        zahl2=int(input()) 
        summe = zahl1 + zahl2
        print("This is your calculation")
        print(zahl1,":",zahl2,"=",summe) 
    else:
        if rechenart == 2:
            print("Whats your first number?")
            zahl1=int(input())
            print("Whats your second number?")
            zahl2=int(input()) 
            summe = zahl1 - zahl2
            print("This is your calculation")
            print(zahl1,":",zahl2,"=",summe) 
        else:
            if rechenart == 3:
                print("Whats your first number?")
                zahl1=int(input())
                print("Whats your second number?")
                zahl2=int(input()) 
                summe = zahl1 * zahl2
                print("This is your calculation")
                print(zahl1,":",zahl2,"=",summe) 
            else:
                if rechenart == 4:
                    print("Whats your first number?")
                    zahl1=int(input())
                    print("Whats your second number?")
                    zahl2=int(input()) 
                    summe = zahl1 / zahl2
                    print("This is your calculation")
                    print(zahl1,":",zahl2,"=",summe)
                else:
                    print("Ungueltige eingabe")     
    print("Do you want to run again")
    print("y/n")
    i=input()
    if i=="y":
        i="y"
    else:
        if  i=="n":
            i="n"
            print("Good bye")
            print("See you soon")
            time.sleep(5)
        else:
            print("Fehler!!!")
            print("Programm wird beendet")
            print("Auf Wiedersehen")
            time.sleep(5)