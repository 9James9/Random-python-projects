import random

computer_score = 0
your_score = 0
while your_score < 3 and computer_score < 3:
  user_choice = input("heads or tails\n")
  coin_flip = random.randint(1,2)
  if coin_flip == 1:
      coin_flip = "heads"
  elif coin_flip == 2:
      coin_flip = "tails"
  if user_choice == coin_flip:
      print("You won!")
      print("The coin landed on: ",coin_flip)
      your_score += 1
      print("Your score is: ",your_score)
  else:
      print("You lose")
      print("The coin landed on: ",coin_flip)
      computer_score += 1
      print("computer's score is: ",computer_score)
if computer_score < your_score:
    print("YOU WON THE COINFLIP TOURNAMENT GRATS")
elif computer_score > your_score:
    print("Better luck next time...")