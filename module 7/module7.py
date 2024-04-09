import os
from msvcrt import getwch

keys = ["H","Q"]

# print("clear screen")
# x = int(input("sudda"))
# if x == 1:


os.system('cls')


while True:
    char = getwch().upper()
    print(char) 
    if char in keys:
        break
print("Jag hoppade ur loopen")