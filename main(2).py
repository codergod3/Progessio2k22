# Problem 2
import sys
i = int(input("Enter the total number of entries:- "))

if i < 1:
    print("ERROR")
    sys.exit()

if i > 1000:
    print("ERROR")
    sys.exit()


for a in range(i):
    x = int(input("Enter Alice height:- "))
    y = int(input("Enter Bob height:- "))

    if x < 100:
        print("ERROR")
        sys.exit()

    if y < 100:
        print("ERROR")
        sys.exit()

    if x > 200:
        print("ERROR")
        sys.exit()

    if y > 200:
        print("ERROR")
        sys.exit()

    if x == y:
        print("ERROR, Both Alice and Bob have the same height")
    if x > y:
        print("Alice(A) is taller")
    if x < y:
        print("Bob(B) is taller")