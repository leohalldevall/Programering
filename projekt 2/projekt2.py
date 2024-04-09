import os
my_list=[]

def add(addition_name):
    my_list.append(addition)

def remove(remove_name):
    my_list.pop(remove)

def listed(edit,name):
    my_list[edit]=name

def result():
    os.system("cls")
    x=0
    print("Din lista")
    for i in my_list:
        x+=1
        print(f"{x}) {i}")
        print("du har",bcolors.blue+str(len(my_list)),bcolors.DEFUALT+ "objekt i din lista")

while True:
    inputx=(input("\nSkriv"))