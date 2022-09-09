import random
import sys
def divide():
    num = 69
    while True:
        try:
            number = random.randint(1,10) - 1
            print(num / number)
        except:
            print("Can't divide by zero. Ending program.")
            sys.exit()
divide()
#This program divides by a number between 0 and 9 until it hits 0 where it exits the program.