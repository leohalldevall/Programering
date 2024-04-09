import math
import random
import os 

#1
os.system("cls")



print("Hej och välkomen, vi ska kolla om du är lång nog för att åka bergodalbanorna på grönalund")

length = int(input(" hur lång är du: "))
if length >= 140:
    print("Du får åka")
elif length <=140:
    print("du får bara åka barn atraktionerna")


#2

x = input("Hej och välkommen vad heter du?: ")
print("hej " + x +"!")
colour = input("vad har du för favoritfärg? ")
while True:
    try:
        age = int(input("hur gammal är du? "))
        break
    except:
        print("fel")





print("\nhej", x, "är du", age, "år gammal, och tycker mest om färgen", colour + "?"), 
o = input(":")
if o == "ja":
    print("trevligt")


#3

print("Dethär är en BMI kalkylator. Låt oss börja med din längd")
while True:
    try:
        weight = int(input("vikt:"))
        break
    except:
        print("fel")
while True: 
    try:
        length = float(input("din längd:"))
        break
    except:
        print("fel")

length = length/100
length = length*2
BMI = weight / length
print ("Du har BMI värdet", BMI)

#4
pi = math.pi
while True:
    try:
        r = float(input("vad är radien: "))
        break
    except:
        print("skriv in din radie med siffror")

r = r*r*pi
round(r)
print("Arean på din cirkel", round(r))

#5

print("här är en miniräknare")
while True:
    calc_method = input(" skrv in ditt räknesätt (+, -, *, /) (eller skriv 'S' för att avsluta): ").upper()
    if calc_method in ("+", "-", "*", "/"):
        pass
    elif calc_method == "S":
        break
    else:
        print ("invalid input")
        continue
    
    if calc_method == "+":
        while True:
            try:
                number1 = float(input("Skriv in det första talet du vill addera med: "))
                break
            except:
                print("invalid input")
        while True:
            try:
                number2 = float(input("Skriv in det andra talet du vill addera med det första talet: "))
                break
            except:
                print("invalid input")
        finalnumber1 = number1 + number2
        print(round(finalnumber1))

    elif calc_method == "-":
        while True:
            try:
                number1 = float(input("Skriv in det första talet du vill subtrahera med: "))
                break
            except:
                print ("invalid input")
        while True:
            try:
                number2 = float(input("Skriv in det andra talet du vill subtrahera med det första talet: "))
                break
            except:
                print("invalid input")
        finalnumber1 = number1-number2
        print(round(finalnumber1))

    elif calc_method == "*":
        while True:
            try:
                number1 = float(input("Skriv in det första talet du vill multiplicera med: "))
                break
            except:
                print("invalid input")
        while True:
            try:
                number2 = float(input("Skriv in det andra talet du vill multiplicera med det första talet: "))
                break
            except:
                print("invalid input")

        finalnumber1 = number1*number2
        print(round(finalnumber1))

    elif calc_method == "/":
        while True:
            try:
                number1 = float(input("Skriv in det första talet du vill dividera med: "))
                break
            except:
                print("invalid input")
        while True:
            try:
                number2 = float(input("Skriv in det andra talet du vill dividera med det första talet: "))
                break
            except:
                print("invalid input")
        finalnumber1 = number1/number2
        print(round(finalnumber1))
        break


#6

print (random.randint(1, 6))

#7
while True:
    try:
        amount = int(input(" välj hur många gånger du vill slå din tärning "))
        break
    except:
        print("invalid input")
for i in range(amount):
	print (random.randint(1, 6))


        
