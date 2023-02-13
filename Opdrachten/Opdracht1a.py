import random
import time

#opdracht_1:
def pyramdie_for():
    rows = int(input("Hoe veel rijen? "))
    for i in range(0, rows):
        for j in range(0, i + 1):
            print("*", end=' ')
        print("\r")
    for i in range(rows, 0, -1):
        for j in range(0, i - 1):
            print("*", end=' ')
        print("\r")
    time.sleep(1)

pyramdie_for()

def pyramide_for_left():
    rows = int(input("Hoe veel rijen? "))
    k = 2 * rows - 2
    for i in range(0, rows - 1):
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
    k = -1
    for i in range(rows - 1, -1, -1):
        for j in range(k, -1, -1):
            print(end=" ")
        k = k + 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")
    time.sleep(1)

pyramide_for_left()

def pyramide_while():
    rows = int(input("Hoe veel rijen? "))
    for i in range(0, rows):
        # This inner loop will print the stars
        for j in range(0, i + 1):
            print("*", end=' ')
            # Change line after each iteration
        print(" ")
        # For second pattern
    for i in range(rows, 0, -1):
        for j in range(0, i - 1):
            print("*", end=' ')
        print(" ")
    time.sleep(1)

pyramide_while()

#opdracht_2:

def compare():
    string_1 = input("Geef een string: ")
    string_2 = input("Geef een string: ")
    if string_1 == string_2:
        print("Geen verschillen gevonden \n")
    else:
        for i in range(len(string_1)):
            if string_1[i] != string_2[i]:
                print("Op index: ", i,",", "verschil: ", string_1[i], string_2[i], "\n")
    time.sleep(1)

compare()

#opdracht_3:

def list_check():
    lst = [1,1,2,2,2,3,3,4,4,45,5,6,67,7,78,8,8,8,9,896,789,76867,67,23]
    print(lst)
    check = lst.count(int(input("Vul een getal in: ")))
    print("Uw ingevoerde getal komt: ", check, "keer voor \n")
    time.sleep(1)

list_check()

def difference():
    lst = [1, 1, 2, 2, 2, 3, 3, 4, 4, 45, 5, 6, 67, 7, 78, 8, 8, 8, 9, 896, 789, 76867, 67, 23]
    max_dif = max([lst[i+1]-lst[i] for i in range(len(lst)-1) if lst[i]<lst[i+1]])
    print(lst, "\n", "Grootste verschil: ", max_dif, "\n")
    time.sleep(1)

difference()

def ones_and_zeros():
    lst = [0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1]
    print(lst)
    check_ones = lst.count(1)
    check_zeros = lst.count(0)
    if check_ones > check_zeros:
        print("Correct \n")
    else:
        print("Error, te veel zero's \n")
    if check_zeros > 12:
        print("Error, meer dan 12 zero's \n")
    time.sleep(1)

ones_and_zeros()

#opdracht_4:

def palindroom():
    woord = input("Woord: ")
    if woord == woord[::-1]:
        print(woord, "is een palindroom \n")
    else:
        print(woord, "is geen palindroom \n")
    time.sleep(1)

palindroom()

#opdracht_5:

def sort():
    lst = [1,24,23,56,42,12,767,890,12,434,134,432,56]
    lst.sort()
    print("Gesoorteerde lijst: ",lst, "\n")
    time.sleep(1)

sort()

#opdracht_6:

def average():
    lst = [1, 24, 23, 56, 42, 12, 767, 890, 12, 434, 134, 432, 56]
    gemiddelde = sum(lst) / len(lst)
    print("Gemiddelde van de lijst lst: ", gemiddelde, "\n")
    time.sleep(1)

average()

#opdracht_7:

def random_number():
    randNum = random.randint(1, 100)
    guesses = 0
    for i in range(1, 8):
        guesses = guesses + 1
        print("Raad een getal tussen 1 en 100! \n")
        guess = input()
        if guess.isdigit():
            if int(guess) > randNum:
                print("Te hoog!")
            elif int(guess) < randNum:
                print("Te laag!")
            elif int(guess) == randNum:
                print("Correct! \n")
                continue
        else:
            print("Invalid Input! Try a number. \n")
    time.sleep(1)


random_number()

#opdracht_8:

def compress():
    with open("textfile.txt") as input:
        with open("textfile_2.txt", "w") as output:
            for line in input:
                output.write(line.lstrip())
    print("Bestand gecompressed")
    time.sleep(1)

compress()

#opdracht_9

def character():
   ch = input("Vul uw waarde in die verschoven moet worden: ")
   n = int(input("Aantal plekken dat de bitjes moeten worden opgeschoven: "))
   if n > 0:
       ch = ch[n:] + ch[:n]
       print(ch, "\n")
   else:
       print(ch[n:] + ch[:n], "\n")
   time.sleep(1)

character()

#opdracht_10

def fibonacci():
    n = int(input("Welk Fibonacci getal zoekt u? ")) + 1
    a = 0
    b = 1
    if n < 0:
        print("Error \n")
    elif n == 0:
        print(a)
    elif n == 1:
        print(b)
    else:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
        print(b)
time.sleep(1)
fibonacci()

#opdracht_11
#write a program for Ceaeser cipher encryption and decryption that uses user input 

def caesar_cipher():
    text = input("Vul uw text in: ")
    shift = int(input("Hoeveel plekken wilt u verschuiven? "))
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    print("Ge-encrypte text: ", result, "\n")
    time.sleep(1)


#opdracht_12

def fizz_buzz():
    for fizzbuzz in range(101):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print("fizzbuzz")
            continue
        elif fizzbuzz % 3 == 0:
            print("fizz")
            continue
        elif fizzbuzz % 5 == 0:
            print("buzz")
            continue
        print(fizzbuzz)
    time.sleep(1)
fizz_buzz()


