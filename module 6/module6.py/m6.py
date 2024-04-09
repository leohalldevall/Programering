"""
def my_function():
    print("hello i'm a function")
my_function()
"""

"""
def my_function(fname):
    print(fname + " Refsnes")

my_function("Leo")
my_function("hannes")
my_function("erik")
"""
"""
def my_function(*fname ,lname):
    print(fname + " " + lname)
my_function("daniel", "refnes")
"""
"""
def my_function(*kids):
    print("bla bla " + kids[1])
my_function("leo", "hej", "gustav")
"""
"""
def my_function(a,b):#function för att summera två tall och get tilbaka dom med ett 
    return a + b

print(my_function(3, 6))
"""
"""
def my_function(fname):# function för att skriva namn
    print(fname + " whoo ")

my_function("Leo")
my_function("hannes")
my_function("erik")

for i in range(10):#loop för att skriva resultatet av en def 10 gånger
    print(my_function("johan rules"))
# Skapa ett program som kan ändra/lägga till/ta bort namn i en lista med olika funktioner
my_list = ["Hannes"]

def list_names():
    print("Mina kompisar")
    for i in my_list:
        print(i)

def add(word):
    my_list.append(word)

def delete(word):
    my_list.remove(word)


while True:
    new_word=input("lägg till namn eller skriv namnet igen om du vill ta bort det: ")
    
    if new_word in my_list:
        delete(new_word)
    elif new_word=="quit":
        break

    else:
        add(new_word)
    
    list_names()


"""


def calc(x,y,op):
    if op==1:
        return x+y 
  
    elif op==2: 
        return x-y   
    
    elif op==3:
        return x*y 

    elif op==4:
        return x/y


print("välkomen till min miniräknare")

while True:
    x=int(input("skriv 1 tal"))
    y=int(input("skriv ett till tal"))
    op=int(input("välj vad du vill göra 1 för +. 2 för -.  3 för *. 4 för division"))
    print(calc( x,y,op))


