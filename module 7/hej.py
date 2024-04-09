import os
from msvcrt import getwch

keys = ["H","Q"]

print("clear screen")
x = int(input("sudda"))
if x == 1:
    os.system('cls')


while True:
    char = getwch()
    print(char)