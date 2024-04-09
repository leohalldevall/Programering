"""
 #Skriv ut något som användaren skriver in 10 gånger med kommandon input() & for loop
 
for x in range(0,10):
    print(str(i+1),"tjena världen animal här") 
x = 0
while True:
    print("halå")
    x = x +1
    if x == 10:

#Skriv ut samtliga heltal mellan 1 och 10

string = input("skriv något som du vill ska sägas 10 gånger ") 
for i in range(0,10):
    print(str(i+1), string)

#Skriv ut samtliga heltal mellan 1 och y

x = int(input("skriv in x "))
for i in range(0,x):
    print(str(i+1))
"""
 #Gör ett program som skriver ut gångertabeller med nästlade for-loopar
for table in range(1, 13):
    print(f"tabell {table}")
    for y in range(1, 11):
        print(f"{table} * {y} = {str(table*y)}")

