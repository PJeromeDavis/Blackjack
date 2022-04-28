############### Blackjack Project #####################

import random
def blackjack():
  try_your_luck=True
  while try_your_luck==True:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    uc_1=random.choice(cards)
    uc_2=random.choice(cards)
    cc_1=random.choice(cards)
    cc_2=random.choice(cards)
    user_cards=[uc_1, uc_2]
    comp_cards=[cc_1, cc_2]

    user_total=sum(user_cards)
    comp_total=sum(comp_cards)
    print(f"Your cards are: {user_cards} and total is: {user_total}")
    print(f"Computer first card is: {cc_1}")
    def card_list(player_cards):
      new_card=random.choice(cards)
      player_cards.append(new_card)
      return player_cards
   
    if user_total==21:
        print(f"You have a blackjack. You won.")
    elif user_total<21:
      if input("Do you want to continue? Press 'y' to hit, press 'n' to stand: ")=="y":
        hit_continue=True
        while hit_continue==True:
          new_user_card_list=card_list(user_cards)
          user_cards=new_user_card_list
          print(f"Your cards are: {user_cards}")
          user_total=sum(user_cards)
          print(f"Your card total is:{user_total}")
          if user_total<21:
            if input("Do you still want to continue? Press 'y' to hit, press 'n' to stand: ")=="n":
              hit_continue=False
          elif user_total==21:
            hit_continue=False
            print(f"Your cards are {user_cards} and total is {user_total}. It's a Blackjack.")
          elif (user_total>21) and (11 in user_cards):
              user_cards.remove(11)
              user_cards.append(1)
              user_total=sum(user_cards)
              if user_total>21:
                  hit_continue=False
                  print(f"Your total is {user_total}. You lost.")
          else :
            hit_continue=False
            print(f"Your cards are {user_cards} and total is {user_total}. You lost.")
    if user_total<21:
      while comp_total<user_total and comp_total<21:
        new_comp_card_list=card_list(comp_cards)
        new_comp_card_total=sum(comp_cards)
        comp_cards=new_comp_card_list
        comp_total=new_comp_card_total
        print(comp_total)

      if user_total==comp_total:
        print("It's a draw.")
      elif user_total<comp_total<=21:
        print(f"The computer wins with a total of {comp_total}.")
      elif comp_total<user_total<=21:
        print(f"You win with a total of {user_total}.")
      else:
        print(f"The computer loses with a total of {comp_total}.")
    if input("Do you want to play a new game of blackjack?. Press 'y' to start or 'n' to stop.")=="n":
      try_your_luck=False


blackjack()




  #print(f"{new_user_cards} total{new_user_total}")
