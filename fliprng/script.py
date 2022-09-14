import random
streak = 0
tries = 0
high_score = 0
def flip():
    output = random.randint(0,1)
    if output == 0:
        return "H"
    elif output == 1:
        return "T"
while streak < 69 and tries != 10000000:
    first = flip()
    second = flip()
    print(first,second)
    if first == second:
        streak += 1
        print("Current streak is: ", streak)
    elif first != second:

        tries += 1
        if streak > high_score:
            high_score = streak
        streak = 0
        print("Failed the streak. Try number: ",tries)
        print("High Score: ",high_score)
print("Program finished.")
#I made this program to visualize the odds of getting Heads or Tails many times in a row. It will run until you end the program, it reaches 69 flips in a row (impossible), or 1,000,000 tries.
#Highest score I've gotten so far: 24