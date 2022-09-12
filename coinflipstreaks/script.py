import random
import locale
from decimal import Decimal
numberOfStreaks = 0
n_runs = 100000
coinFlip = []
streak = 0
high_score = 0
flips_per_run = 100
total_instances = n_runs * flips_per_run
def f(d):
    return '{0:n}'.format(d)
locale.setlocale(locale.LC_ALL, 'en_us')
for experimentNumber in range(n_runs):
    coinFlip = []
    notification_threshhold = 10000
    if experimentNumber % notification_threshhold == 0:
        print('Flip number: ' + str(f(Decimal(experimentNumber * flips_per_run))))
    for i in range(flips_per_run):
        coinFlip.append(random.randint(0,1))
        if i==0:
            pass
        elif coinFlip[i] == coinFlip[i - 1]:
            streak += 1
        else:
            streak = 0
        if streak == 6:
            numberOfStreaks += 1
        if streak > high_score:
            high_score = streak
odds_of_high_score = 2 ** high_score
print('High score: '+  str(high_score) +'\n' + "The odds of receiving this high score are 1 in " + str(f(Decimal(odds_of_high_score))) + '\nNumber of 6+ streaks: ' + str(numberOfStreaks))

# print("The odds of receiving this high score are 1 in " + str(odds_of_high_score))
total_runs = n_runs * flips_per_run

odds = (numberOfStreaks / total_runs) * 100
print('There was a ' + str(round(odds,2)) + '% chance of receiving a 6+ streak')
    
    
    
