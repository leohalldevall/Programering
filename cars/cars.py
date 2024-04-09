import os

my_cars=["911 gtrs", "koenigsegg jesko absolut"]

looping = True

while looping:

    os.system("cls")

    print("välkommen")

    #ta emot nytt namn och spara i listan
    #ta bort namn från listan och spara
    #Ändra namn i listan
    #kunna avsluta program
    #lista namnen

    # print(my_cars[0])

    no=1

    for n in my_cars:
        print(str(no)+")",n)
        no += 1

    new_car=input("nämn en ny bil: ")
    
    if new_car.isdigit():
        print("vill du ta bort (t) eller redigera (r): " ,my_cars[int(new_car)-1])
        input:()
    if input == (t):
        my_cars.pop(t)

        print(new_car)
        my_cars.pop(int(new_car)-1)
    else:
        my_cars.append(new_car)
    