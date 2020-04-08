
from random import choice
import time

def botace():
    raise no
def userace(usercard):
    raise no

def bot():
    if black.botstop == False:
        if black.user_has_stopped == True and abs(21-black.bottotal) < abs(21-black.usertotal) \
           or black.user_has_stopped == False and black.bottotal > 16:
            
            black.botstop = True
            
        elif black.bottotal < 21 and abs(21-black.bottotal) > abs(21-black.usertotal)\
           or black.bottotal < 16:
            botcard = choice(black.cards)
            black.cards.remove(botcard)
            #if botace(botcard):
            #   botcard = 11
                    
            black.bottotal += botcard
            print(f"Bot now has {black.bottotal} in hand\n")
            
        else:
            black.botstop = True
    if black.botstop == True:
        print(f"bot stopped at {black.bottotal}\n")
        
    
def user():
    if black.usertotal > 21:
        black.user_has_stopped = True
        
        print(f"\nyou have more than 21...")
        time.sleep(0.8)
        
    while black.user_has_stopped == False and black.usertotal < 21 :
        user.goornot = input('go or no')
        
        if user.goornot == 'go':
            time.sleep(0.8)
            usercard = choice(black.cards)
            black.cards.remove(usercard)
            #if userace(usercard):
            #   usercard = 11
            
            black.usertotal += usercard
            print(f"\nyou have now {black.usertotal} in hand")
            break
        elif user.goornot == 'no':
            black.user_has_stopped = True
            break
    
    
        
def stopped():       
    if black.botstop == True and black.user_has_stopped == True:
        return True

def judge():
    time.sleep(1)
    if abs((21-black.bottotal)) < abs((21-black.usertotal)):
        return "bot won"
    
    elif abs((21-black.bottotal)) >  abs((21-black.usertotal)):
        
        return "user won"
    
    else:
        return "tie "
        
def twen():
    if black.usertotal == 21 or black.bottotal == 21:
        return True
    
def check():
    if twen() == True or stopped() == True:
        return True
    
def black():
    print("""\ntry to reach 21! you will compete against a bot
earn 25 points if you win, earn 10 points if you tie
(if you go past 21, you will be restricted from going once more)\n""")
    black.score = 0
    play = True
    while play == True:
        black.cards=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
      1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
      1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
      1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        black.usertotal = 0
        black.bottotal = 0
        black.user_has_stopped = False
        black.botstop = False
        
        while True:
            
            if check():
                break
            user()
            if check():
                break 
            bot()
            if check():
                break
        print(judge())
        if judge() != 2:
            black.score+=100
        choi = input("\n1 to leave, any to stay")
        if choi == "1":
            play = False
    print(f"you earned {black.score} points")
    return black.score


